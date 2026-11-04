# Range-Scalp Bot

*Updated Wed Nov 04 21:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47550 | 41404 | 6146 (73) | 2 | $-13714.49 | -4.6% |
| **+10¢** | 35526 | 28397 | 7129 (98) | 2 | $-12531.64 | -5.6% |
| **+15¢** | 29759 | 22082 | 7677 (126) | 3 | $-11484.75 | -6.1% |
| **+20¢** | 26442 | 18401 | 8041 (166) | 3 | $-10141.16 | -6.1% |
| **+10¢ (15¢ stop)** | 57957 | 57864 | 93 (56) | 1 | $-21590.89 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 21:20 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 11-04 21:17 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-04 21:17 | +10 stop | XRP | DOWN | 0.65 | 0.48 | -2.04 |
| 11-04 21:17 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-04 21:17 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 21:17 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-04 21:17 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-04 21:17 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 21:17 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-04 21:17 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-04 21:17 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 21:17 | +15 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 11-04 21:17 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 21:17 | +5 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 21:16 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 21:16 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-04 21:16 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-04 21:16 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 21:16 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-04 21:16 | +10 stop | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 21:16 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-04 21:16 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 21:16 | +10 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 11-04 21:16 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-04 21:15 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-04 21:15 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-04 21:15 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-04 21:15 | +10 | HYPE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-04 21:15 | +5 | HYPE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-04 21:15 | +10 stop | XRP | UP | 0.60 | 0.44 | -1.95 |
| 11-04 21:15 | +20 | XRP | UP | 0.60 | open |  |
| 11-04 21:15 | +15 | XRP | UP | 0.60 | open |  |
| 11-04 21:15 | +10 | XRP | UP | 0.61 | open |  |
| 11-04 21:15 | +5 | XRP | UP | 0.61 | open |  |
| 11-04 21:15 | +10 stop | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-04 21:15 | +20 | ETH | DOWN | 0.61 | 0.83 | 1.93 |
| 11-04 21:15 | +15 | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 11-04 21:15 | +10 | ETH | DOWN | 0.61 | 0.73 | 0.89 |
| 11-04 21:15 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-04 21:15 | +10 stop | NEAR | UP | 0.55 | 0.38 | -2.05 |
