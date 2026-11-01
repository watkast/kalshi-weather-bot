# Range-Scalp Bot

*Updated Sun Nov 01 10:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43504 | 37911 | 5593 (63) | 6 | $-12411.93 | -4.5% |
| **+10¢** | 32458 | 25998 | 6460 (85) | 5 | $-11114.82 | -5.4% |
| **+15¢** | 27164 | 20206 | 6958 (112) | 7 | $-10152.57 | -6.0% |
| **+20¢** | 24123 | 16836 | 7287 (146) | 8 | $-8949.09 | -5.9% |
| **+10¢ (15¢ stop)** | 53081 | 52996 | 85 (50) | 0 | $-20067.32 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 10:56 | +10 stop | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 11-01 10:56 | +10 stop | SOL | UP | 0.58 | 0.70 | 0.87 |
| 11-01 10:56 | +20 | SOL | UP | 0.59 | open |  |
| 11-01 10:56 | +15 | SOL | UP | 0.59 | open |  |
| 11-01 10:56 | +10 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 11-01 10:55 | +10 stop | DOGE | DOWN | 0.40 | 0.59 | 1.56 |
| 11-01 10:55 | +10 stop | ZEC | UP | 0.56 | 0.67 | 0.76 |
| 11-01 10:54 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 10:54 | +10 stop | DOGE | UP | 0.68 | 0.45 | -2.64 |
| 11-01 10:54 | +15 | DOGE | UP | 0.68 | open |  |
| 11-01 10:54 | +10 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-01 10:54 | +5 | DOGE | UP | 0.68 | 0.80 | 0.92 |
| 11-01 10:53 | +10 stop | ETH | DOWN | 0.57 | 0.82 | 2.21 |
| 11-01 10:52 | +5 | ETH | UP | 0.58 | open |  |
| 11-01 10:52 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 10:52 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 11-01 10:52 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 11-01 10:52 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 10:52 | +5 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 10:51 | +5 | ETH | UP | 0.57 | 0.68 | 0.76 |
| 11-01 10:51 | +10 stop | ZEC | UP | 0.53 | 0.70 | 1.37 |
| 11-01 10:50 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 10:50 | +5 | ETH | UP | 0.60 | 0.69 | 0.58 |
| 11-01 10:50 | +10 stop | XRP | UP | 0.65 | 0.27 | -4.10 |
| 11-01 10:49 | +10 stop | BTC | DOWN | 0.53 | 0.68 | 1.16 |
| 11-01 10:49 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-01 10:49 | +10 stop | ETH | UP | 0.62 | 0.42 | -2.35 |
| 11-01 10:49 | +10 stop | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 11-01 10:49 | +10 stop | ETH | DOWN | 0.37 | 0.60 | 1.96 |
| 11-01 10:49 | +10 stop | ZEC | DOWN | 0.61 | 0.44 | -2.05 |
| 11-01 10:49 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-01 10:49 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-01 10:48 | +10 stop | SOL | DOWN | 0.52 | 0.33 | -2.24 |
| 11-01 10:48 | +5 | SOL | DOWN | 0.54 | open |  |
| 11-01 10:48 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-01 10:48 | +10 stop | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 10:48 | +15 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 10:48 | +10 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 10:48 | +5 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-01 10:47 | +10 stop | SOL | UP | 0.59 | 0.44 | -1.85 |
