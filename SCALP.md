# Range-Scalp Bot

*Updated Tue Oct 13 11:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14560 | 12590 | 1970 (27) | 1 | $-4711.96 | -5.1% |
| **+10¢** | 11019 | 8732 | 2287 (39) | 2 | $-4422.19 | -6.4% |
| **+15¢** | 9262 | 6816 | 2446 (57) | 2 | $-3930.04 | -6.8% |
| **+20¢** | 8241 | 5695 | 2546 (72) | 4 | $-3377.15 | -6.5% |
| **+10¢ (15¢ stop)** | 17872 | 17823 | 49 (29) | 0 | $-6949.29 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 11:22 | +10 stop | NEAR | DOWN | 0.34 | 0.53 | 1.56 |
| 10-13 11:22 | +20 | NEAR | DOWN | 0.34 | open |  |
| 10-13 11:22 | +15 | NEAR | DOWN | 0.34 | 0.53 | 1.56 |
| 10-13 11:22 | +10 | NEAR | DOWN | 0.34 | 0.53 | 1.56 |
| 10-13 11:22 | +5 | NEAR | DOWN | 0.35 | 0.53 | 1.46 |
| 10-13 11:21 | +10 stop | BNB | DOWN | 0.32 | 0.53 | 1.76 |
| 10-13 11:21 | +10 | BNB | DOWN | 0.32 | 0.53 | 1.76 |
| 10-13 11:21 | +5 | BNB | DOWN | 0.32 | 0.53 | 1.76 |
| 10-13 11:20 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.51 |
| 10-13 11:20 | +15 | SOL | DOWN | 0.67 | open |  |
| 10-13 11:20 | +10 | SOL | DOWN | 0.68 | open |  |
| 10-13 11:20 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-13 11:20 | +10 stop | BTC | DOWN | 0.56 | 0.39 | -2.05 |
| 10-13 11:20 | +10 | BTC | DOWN | 0.53 | open |  |
| 10-13 11:20 | +5 | BTC | DOWN | 0.52 | 0.58 | 0.24 |
| 10-13 11:18 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-13 11:18 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-13 11:18 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-13 11:17 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 11:17 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 11:17 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 10-13 11:17 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 11:17 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 11:17 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-13 11:16 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-13 11:16 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-13 11:16 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-13 11:16 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 0.99 |
| 10-13 11:16 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-13 11:16 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-13 11:16 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-13 11:16 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 11:16 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-13 11:16 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-13 11:16 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 11:16 | +10 stop | BNB | UP | 0.45 | 0.57 | 0.84 |
