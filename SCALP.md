# Range-Scalp Bot

*Updated Sun Nov 08 11:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52433 | 45712 | 6721 (83) | 3 | $-14541.32 | -4.4% |
| **+10¢** | 39138 | 31306 | 7832 (108) | 3 | $-13527.87 | -5.5% |
| **+15¢** | 32788 | 24346 | 8442 (138) | 2 | $-12402.04 | -6.0% |
| **+20¢** | 29163 | 20317 | 8846 (182) | 3 | $-10907.15 | -6.0% |
| **+10¢ (15¢ stop)** | 63849 | 63743 | 106 (63) | 0 | $-23630.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 11:58 | +10 stop | BNB | UP | 0.58 | 0.88 | 2.70 |
| 11-08 11:58 | +15 | SOL | UP | 0.65 | 0.90 | 2.27 |
| 11-08 11:57 | +10 stop | SOL | UP | 0.68 | 0.90 | 1.97 |
| 11-08 11:57 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-08 11:57 | +10 stop | SOL | DOWN | 0.68 | 0.42 | -2.94 |
| 11-08 11:57 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-08 11:56 | +10 stop | BNB | DOWN | 0.66 | 0.18 | -5.07 |
| 11-08 11:56 | +10 stop | SOL | UP | 0.48 | 0.60 | 0.85 |
| 11-08 11:56 | +10 | SOL | UP | 0.48 | 0.60 | 0.85 |
| 11-08 11:55 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 11-08 11:55 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-08 11:55 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 11:55 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 11-08 11:55 | +10 stop | BNB | UP | 0.64 | 0.40 | -2.74 |
| 11-08 11:54 | +10 stop | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 11-08 11:54 | +10 stop | SOL | DOWN | 0.56 | 0.39 | -2.05 |
| 11-08 11:54 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 11-08 11:53 | +10 stop | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 11-08 11:53 | +5 | ZEC | UP | 0.66 | 0.76 | 0.73 |
| 11-08 11:52 | +5 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 11-08 11:52 | +10 stop | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-08 11:52 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-08 11:52 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 11-08 11:51 | +10 stop | ETH | UP | 0.66 | 0.47 | -2.24 |
| 11-08 11:51 | +10 | ETH | UP | 0.66 | 0.91 | 2.29 |
| 11-08 11:51 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 11-08 11:51 | +10 stop | XRP | DOWN | 0.51 | 0.69 | 1.47 |
| 11-08 11:51 | +20 | XRP | DOWN | 0.52 | 0.78 | 2.29 |
| 11-08 11:51 | +15 | XRP | DOWN | 0.52 | 0.69 | 1.37 |
| 11-08 11:51 | +5 | XRP | DOWN | 0.52 | 0.58 | 0.24 |
| 11-08 11:51 | +10 stop | BNB | DOWN | 0.53 | 0.30 | -2.63 |
| 11-08 11:51 | +20 | BNB | DOWN | 0.55 | open |  |
| 11-08 11:51 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-08 11:51 | +10 stop | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 11-08 11:51 | +10 | DOGE | UP | 0.60 | 0.78 | 1.50 |
| 11-08 11:51 | +5 | DOGE | UP | 0.60 | 0.67 | 0.37 |
| 11-08 11:51 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.03 |
| 11-08 11:50 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 11-08 11:50 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 11-08 11:49 | +5 | BNB | DOWN | 0.70 | open |  |
