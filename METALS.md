# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 1:51 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 113 | 111 | 38 (34%) | 39¢ | 47% | -$72.48 | -16% |
| Silver | 57 | 56 | 18 (32%) | 34¢ | 42% | -$19.21 | -10% |
| Gold | 56 | 55 | 20 (36%) | 44¢ | 52% | -$53.27 | -21% |

*Earlier half -$41.03 / later half -$31.45.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 114 | 39 (34%) | -$86.19 | -18% |
| 4¢+ ← live bot | 111 | 40 (36%) | -$16.07 | -4% |
| 6¢+ | 99 | 42 (42%) | $80.35 | +24% |
| 8¢+ | 86 | 37 (43%) | $95.08 | +35% |
| 10¢+ | 73 | 28 (38%) | $58.60 | +26% |
| 15¢+ | 43 | 16 (37%) | $48.50 | +43% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2840 | -0.5% |
| Hyperliquid price vs Kalshi's target | 2840 | +2.1% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | Open | — |
| 9/29 1:46:02 PM | Gold | UP | 13.9 min | 30¢ | 50% | 18¢ | Open | — |
| 9/29 1:33:34 PM | Silver | UP | 11.4 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/29 1:31:03 PM | Gold | UP | 13.9 min | 36¢ | 50% | 12¢ | ✅ Won | $6.23 |
| 9/29 1:19:47 PM | Silver | DOWN | 10.2 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 1:16:19 PM | Gold | DOWN | 13.7 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/29 1:02:33 PM | Gold | UP | 12.4 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.27 |
| 9/29 1:02:03 PM | Silver | UP | 12.9 min | 41¢ | 47% | 4¢ | ❌ Lost | -$4.27 |
| 9/29 12:46:21 PM | Gold | UP | 13.7 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 12:46:03 PM | Silver | UP | 13.9 min | 39¢ | 50% | 9¢ | ✅ Won | $5.93 |
| 9/29 12:33:37 PM | Gold | UP | 11.4 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 12:32:31 PM | Silver | UP | 12.5 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
