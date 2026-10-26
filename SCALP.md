# Range-Scalp Bot

*Updated Mon Oct 26 00:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33952 | 29643 | 4309 (43) | 3 | $-9379.97 | -4.4% |
| **+10¢** | 25416 | 20432 | 4984 (65) | 3 | $-8222.78 | -5.1% |
| **+15¢** | 21260 | 15896 | 5364 (89) | 3 | $-7338.39 | -5.5% |
| **+20¢** | 18840 | 13224 | 5616 (111) | 3 | $-6413.08 | -5.4% |
| **+10¢ (15¢ stop)** | 41592 | 41530 | 62 (33) | 0 | $-15816.34 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 00:10 | +10 stop | ZEC | DOWN | 0.51 | 0.72 | 1.77 |
| 10-26 00:10 | +20 | ZEC | DOWN | 0.51 | 0.72 | 1.77 |
| 10-26 00:10 | +15 | ZEC | DOWN | 0.51 | 0.72 | 1.77 |
| 10-26 00:10 | +10 | ZEC | DOWN | 0.51 | 0.72 | 1.77 |
| 10-26 00:10 | +5 | ZEC | DOWN | 0.51 | 0.59 | 0.45 |
| 10-26 00:09 | +10 stop | BNB | UP | 0.69 | 0.93 | 2.24 |
| 10-26 00:09 | +10 stop | ETH | UP | 0.65 | 0.79 | 1.12 |
| 10-26 00:08 | +10 stop | BNB | DOWN | 0.57 | 0.36 | -2.45 |
| 10-26 00:07 | +10 stop | BTC | DOWN | 0.69 | 0.49 | -2.33 |
| 10-26 00:07 | +10 | BTC | DOWN | 0.69 | open |  |
| 10-26 00:07 | +5 | BTC | DOWN | 0.69 | open |  |
| 10-26 00:07 | +10 stop | NEAR | UP | 0.52 | 0.63 | 0.75 |
| 10-26 00:07 | +5 | NEAR | UP | 0.52 | 0.63 | 0.75 |
| 10-26 00:07 | +10 stop | ETH | DOWN | 0.64 | 0.48 | -1.95 |
| 10-26 00:07 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-26 00:07 | +10 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 10-26 00:07 | +5 | DOGE | UP | 0.60 | 0.76 | 1.30 |
| 10-26 00:07 | +10 stop | HYPE | UP | 0.60 | 0.74 | 1.09 |
| 10-26 00:07 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-26 00:07 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 10-26 00:07 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 10-26 00:07 | +10 stop | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 10-26 00:07 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 10-26 00:06 | +10 stop | BTC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-26 00:06 | +10 | BTC | DOWN | 0.52 | 0.69 | 1.37 |
| 10-26 00:06 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 10-26 00:06 | +10 | ETH | DOWN | 0.61 | open |  |
| 10-26 00:06 | +5 | ETH | DOWN | 0.61 | 0.69 | 0.48 |
| 10-26 00:06 | +10 stop | NEAR | DOWN | 0.57 | 0.38 | -2.22 |
| 10-26 00:05 | +10 stop | HYPE | DOWN | 0.68 | 0.45 | -2.64 |
| 10-26 00:05 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-26 00:05 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-26 00:05 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.85 |
| 10-26 00:04 | +10 stop | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 10-26 00:04 | +15 | HYPE | DOWN | 0.54 | open |  |
| 10-26 00:04 | +10 | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 10-26 00:04 | +5 | HYPE | DOWN | 0.54 | 0.68 | 1.02 |
| 10-26 00:04 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.87 |
| 10-26 00:04 | +10 stop | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-26 00:04 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
