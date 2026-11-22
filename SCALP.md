# Range-Scalp Bot

*Updated Sun Nov 22 14:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68828 | 60067 | 8761 (142) | 2 | $-18465.30 | -4.3% |
| **+10¢** | 51361 | 41129 | 10232 (186) | 3 | $-17107.36 | -5.3% |
| **+15¢** | 43044 | 32012 | 11032 (237) | 3 | $-15363.06 | -5.7% |
| **+20¢** | 38322 | 26731 | 11591 (295) | 4 | $-13667.79 | -5.7% |
| **+10¢ (15¢ stop)** | 83799 | 83614 | 185 (116) | 2 | $-30848.25 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 14:36 | +5 | ETH | UP | 0.60 | open |  |
| 11-22 14:35 | +10 stop | BNB | UP | 0.61 | open |  |
| 11-22 14:35 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 11-22 14:34 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 11-22 14:33 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-22 14:33 | +10 | ETH | UP | 0.60 | open |  |
| 11-22 14:33 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 11-22 14:33 | +10 stop | SOL | UP | 0.63 | 0.81 | 1.52 |
| 11-22 14:33 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 11-22 14:33 | +10 stop | BNB | UP | 0.57 | 0.70 | 0.97 |
| 11-22 14:33 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-22 14:33 | +20 | XRP | UP | 0.66 | 0.86 | 1.75 |
| 11-22 14:33 | +15 | XRP | UP | 0.66 | 0.81 | 1.23 |
| 11-22 14:33 | +10 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 11-22 14:33 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-22 14:33 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 11-22 14:33 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-22 14:32 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-22 14:32 | +20 | DOGE | UP | 0.67 | open |  |
| 11-22 14:32 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 11-22 14:32 | +10 | DOGE | UP | 0.67 | 0.79 | 0.92 |
| 11-22 14:32 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 11-22 14:32 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 11-22 14:32 | +10 stop | ZEC | UP | 0.59 | 0.73 | 1.06 |
| 11-22 14:32 | +20 | ZEC | UP | 0.59 | 0.84 | 2.20 |
| 11-22 14:32 | +15 | ZEC | UP | 0.59 | 0.75 | 1.26 |
| 11-22 14:32 | +10 | ZEC | UP | 0.59 | 0.73 | 1.06 |
| 11-22 14:32 | +5 | ZEC | UP | 0.59 | 0.66 | 0.34 |
| 11-22 14:32 | +10 stop | BNB | DOWN | 0.55 | 0.40 | -1.85 |
| 11-22 14:32 | +20 | BNB | DOWN | 0.55 | open |  |
| 11-22 14:32 | +15 | BNB | DOWN | 0.55 | open |  |
| 11-22 14:32 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-22 14:32 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-22 14:31 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-22 14:31 | +20 | NEAR | UP | 0.71 | 0.91 | 1.80 |
| 11-22 14:31 | +15 | NEAR | UP | 0.71 | 0.87 | 1.37 |
| 11-22 14:31 | +10 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-22 14:31 | +5 | NEAR | UP | 0.71 | 0.81 | 0.74 |
| 11-22 14:31 | +10 stop | ETH | UP | 0.56 | 0.68 | 0.86 |
| 11-22 14:31 | +20 | ETH | UP | 0.56 | open |  |
