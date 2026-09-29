# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 1:11 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 107 | 105 | 36 (34%) | 39¢ | 47% | -$68.27 | -16% |
| Silver | 54 | 53 | 17 (32%) | 34¢ | 42% | -$17.82 | -9% |
| Gold | 53 | 52 | 19 (37%) | 45¢ | 52% | -$50.45 | -21% |

*Earlier half -$43.43 / later half -$24.84.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 108 | 37 (34%) | -$81.26 | -18% |
| 4¢+ ← live bot | 105 | 38 (36%) | -$12.77 | -3% |
| 6¢+ | 93 | 39 (42%) | $72.23 | +23% |
| 8¢+ | 80 | 35 (44%) | $94.07 | +37% |
| 10¢+ | 67 | 26 (39%) | $55.41 | +27% |
| 15¢+ | 40 | 15 (38%) | $48.16 | +47% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2690 | +0.0% |
| Hyperliquid price vs Kalshi's target | 2690 | +2.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:02:33 PM | Gold | UP | 12.4 min | 41¢ | 48% | 5¢ | Open | — |
| 9/29 1:02:03 PM | Silver | UP | 12.9 min | 41¢ | 47% | 4¢ | Open | — |
| 9/29 12:46:21 PM | Gold | UP | 13.7 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 12:46:03 PM | Silver | UP | 13.9 min | 39¢ | 50% | 9¢ | ✅ Won | $5.93 |
| 9/29 12:33:37 PM | Gold | UP | 11.4 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 12:32:31 PM | Silver | UP | 12.5 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/29 12:22:09 PM | Silver | UP | 7.8 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/29 12:16:11 PM | Gold | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 12:01:02 PM | Gold | UP | 13.9 min | 91¢ | 96% | 4¢ | ✅ Won | $0.84 |
| 9/29 11:47:34 AM | Silver | UP | 12.4 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/29 11:46:56 AM | Gold | UP | 13.1 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 11:32:32 AM | Gold | UP | 12.4 min | 34¢ | 46% | 10¢ | ❌ Lost | -$3.56 |
