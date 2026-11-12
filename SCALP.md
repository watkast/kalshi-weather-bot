# Range-Scalp Bot

*Updated Thu Nov 12 19:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57138 | 49811 | 7327 (101) | 3 | $-15708.83 | -4.4% |
| **+10¢** | 42714 | 34162 | 8552 (133) | 3 | $-14660.54 | -5.5% |
| **+15¢** | 35808 | 26602 | 9206 (167) | 3 | $-13272.29 | -5.9% |
| **+20¢** | 31902 | 22243 | 9659 (217) | 3 | $-11639.78 | -5.8% |
| **+10¢ (15¢ stop)** | 69687 | 69559 | 128 (78) | 2 | $-25721.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 19:08 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-12 19:08 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-12 19:08 | +10 stop | ZEC | DOWN | 0.53 | 0.67 | 1.06 |
| 11-12 19:06 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 11-12 19:06 | +20 | NEAR | DOWN | 0.67 | open |  |
| 11-12 19:06 | +15 | NEAR | DOWN | 0.67 | open |  |
| 11-12 19:06 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-12 19:06 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-12 19:06 | +10 stop | ZEC | DOWN | 0.50 | 0.61 | 0.75 |
| 11-12 19:03 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-12 19:02 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 11-12 19:02 | +20 | ZEC | UP | 0.60 | open |  |
| 11-12 19:02 | +15 | ZEC | UP | 0.60 | open |  |
| 11-12 19:02 | +10 | ZEC | UP | 0.60 | open |  |
| 11-12 19:02 | +5 | ZEC | UP | 0.60 | open |  |
| 11-12 19:01 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 11-12 19:01 | +20 | SOL | DOWN | 0.71 | 0.93 | 1.98 |
| 11-12 19:01 | +15 | SOL | DOWN | 0.71 | 0.89 | 1.58 |
| 11-12 19:01 | +10 | SOL | DOWN | 0.71 | 0.85 | 1.16 |
| 11-12 19:01 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 11-12 19:01 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 19:01 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-12 19:01 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-12 19:01 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 19:01 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-12 19:01 | +10 stop | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 19:01 | +20 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 11-12 19:01 | +15 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 11-12 19:01 | +10 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 19:01 | +5 | NEAR | DOWN | 0.63 | 0.76 | 1.00 |
| 11-12 19:01 | +10 stop | HYPE | DOWN | 0.58 | 0.79 | 1.80 |
| 11-12 19:01 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-12 19:00 | +10 stop | HYPE | UP | 0.46 | 0.56 | 0.64 |
| 11-12 19:00 | +20 | HYPE | UP | 0.46 | open |  |
| 11-12 19:00 | +15 | HYPE | UP | 0.46 | open |  |
| 11-12 19:00 | +10 | HYPE | UP | 0.48 | open |  |
| 11-12 19:00 | +5 | HYPE | UP | 0.48 | 0.56 | 0.44 |
| 11-12 18:57 | +10 stop | ZEC | DOWN | 0.45 | 0.63 | 1.45 |
| 11-12 18:57 | +10 | DOGE | DOWN | 0.44 | yes | -4.58 |
| 11-12 18:57 | +5 | DOGE | DOWN | 0.48 | 0.53 | 0.14 |
