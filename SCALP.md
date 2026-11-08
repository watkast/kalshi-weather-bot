# Range-Scalp Bot

*Updated Sun Nov 08 16:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52519 | 45782 | 6737 (83) | 1 | $-14599.47 | -4.4% |
| **+10¢** | 39206 | 31358 | 7848 (108) | 1 | $-13568.50 | -5.5% |
| **+15¢** | 32847 | 24388 | 8459 (138) | 1 | $-12442.55 | -6.0% |
| **+20¢** | 29218 | 20354 | 8864 (182) | 2 | $-10939.27 | -6.0% |
| **+10¢ (15¢ stop)** | 63965 | 63859 | 106 (63) | 1 | $-23709.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 16:38 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-08 16:36 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 11-08 16:35 | +10 stop | DOGE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-08 16:35 | +10 stop | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 11-08 16:34 | +10 stop | XRP | UP | 0.54 | 0.36 | -2.15 |
| 11-08 16:33 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-08 16:33 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-08 16:33 | +15 | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 11-08 16:33 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-08 16:33 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-08 16:33 | +10 stop | DOGE | UP | 0.66 | 0.47 | -2.24 |
| 11-08 16:32 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 11-08 16:32 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 16:32 | +20 | HYPE | DOWN | 0.63 | 0.87 | 2.15 |
| 11-08 16:32 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 16:32 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 16:32 | +5 | HYPE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-08 16:32 | +10 stop | XRP | DOWN | 0.71 | 0.49 | -2.53 |
| 11-08 16:32 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-08 16:32 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-08 16:32 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-08 16:32 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-08 16:31 | +10 stop | DOGE | DOWN | 0.57 | 0.38 | -2.25 |
| 11-08 16:31 | +20 | DOGE | DOWN | 0.57 | 0.84 | 2.42 |
| 11-08 16:31 | +15 | DOGE | DOWN | 0.57 | 0.84 | 2.42 |
| 11-08 16:31 | +10 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-08 16:31 | +5 | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-08 16:31 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-08 16:31 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-08 16:31 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-08 16:31 | +10 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-08 16:31 | +5 | BNB | DOWN | 0.69 | 0.81 | 0.94 |
| 11-08 16:31 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-08 16:31 | +20 | SOL | DOWN | 0.65 | 0.89 | 2.17 |
| 11-08 16:31 | +15 | SOL | DOWN | 0.65 | 0.84 | 1.64 |
| 11-08 16:31 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 11-08 16:31 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 11-08 16:31 | +10 stop | NEAR | DOWN | 0.68 | 0.51 | -2.04 |
| 11-08 16:31 | +20 | NEAR | DOWN | 0.62 | 0.85 | 2.04 |
| 11-08 16:31 | +15 | NEAR | DOWN | 0.62 | 0.81 | 1.62 |
