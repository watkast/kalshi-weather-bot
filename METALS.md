# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:01 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 99 | 98 | 30 (31%) | 39¢ | 47% | -$98.06 | -25% |
| Silver | 50 | 50 | 15 (30%) | 34¢ | 42% | -$27.34 | -15% |
| Gold | 49 | 48 | 15 (31%) | 44¢ | 52% | -$70.72 | -32% |

*Earlier half -$41.01 / later half -$57.05.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 101 | 31 (31%) | -$109.51 | -26% |
| 4¢+ ← live bot | 98 | 32 (33%) | -$43.46 | -12% |
| 6¢+ | 87 | 34 (39%) | $41.33 | +14% |
| 8¢+ | 74 | 30 (41%) | $61.94 | +26% |
| 10¢+ | 61 | 22 (36%) | $31.43 | +17% |
| 15¢+ | 34 | 13 (38%) | $39.72 | +44% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2484 | -1.6% |
| Hyperliquid price vs Kalshi's target | 2484 | +1.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:01:02 PM | Gold | UP | 13.9 min | 91¢ | 96% | 4¢ | Open | — |
| 9/29 11:47:34 AM | Silver | UP | 12.4 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/29 11:46:56 AM | Gold | UP | 13.1 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 11:32:32 AM | Gold | UP | 12.4 min | 34¢ | 46% | 10¢ | ❌ Lost | -$3.56 |
| 9/29 11:32:10 AM | Silver | UP | 12.8 min | 32¢ | 41% | 7¢ | ❌ Lost | -$3.36 |
| 9/29 11:19:27 AM | Gold | DOWN | 10.5 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
| 9/29 11:16:05 AM | Silver | DOWN | 13.9 min | 41¢ | 48% | 6¢ | ❌ Lost | -$4.27 |
| 9/29 11:01:35 AM | Silver | DOWN | 13.4 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/29 11:01:13 AM | Gold | DOWN | 13.8 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 10:50:18 AM | Silver | DOWN | 9.7 min | 29¢ | 36% | 6¢ | ✅ Won | $6.95 |
| 9/29 10:46:06 AM | Gold | UP | 13.9 min | 32¢ | 39% | 6¢ | ❌ Lost | -$3.36 |
| 9/29 10:38:20 AM | Gold | UP | 6.7 min | 48¢ | 55% | 5¢ | ❌ Lost | -$4.98 |
