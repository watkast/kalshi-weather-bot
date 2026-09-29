# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:21 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 42 | 40 | 15 (38%) | 40¢ | 48% | -$16.75 | -10% |
| Silver | 21 | 20 | 6 (30%) | 34¢ | 42% | -$10.55 | -15% |
| Gold | 21 | 20 | 9 (45%) | 46¢ | 54% | -$6.20 | -6% |

*Earlier half $22.76 / later half -$39.51.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 40 | 12 (30%) | -$50.41 | -30% |
| 4¢+ ← live bot | 39 | 13 (33%) | -$13.25 | -9% |
| 6¢+ | 36 | 12 (33%) | $4.22 | +4% |
| 8¢+ | 32 | 12 (38%) | $26.28 | +28% |
| 10¢+ | 28 | 8 (29%) | $7.37 | +10% |
| 15¢+ | 14 | 5 (36%) | $18.25 | +57% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 999 | -5.2% |
| Hyperliquid price vs Kalshi's target | 999 | -11.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | Open | — |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | Open | — |
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | ❌ Lost | -$3.77 |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | ❌ Lost | -$3.46 |
| 9/28 11:34:38 PM | Silver | DOWN | 10.4 min | 81¢ | 92% | 10¢ | ❌ Lost | -$8.21 |
| 9/28 11:31:34 PM | Gold | DOWN | 13.4 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | ✅ Won | $7.05 |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
