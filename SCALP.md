# Range-Scalp Bot

*Updated Thu Oct 29 21:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39760 | 34718 | 5042 (50) | 3 | $-10989.55 | -4.4% |
| **+10¢** | 29643 | 23812 | 5831 (73) | 4 | $-9737.75 | -5.2% |
| **+15¢** | 24787 | 18514 | 6273 (100) | 4 | $-8745.33 | -5.6% |
| **+20¢** | 21995 | 15422 | 6573 (129) | 6 | $-7632.99 | -5.5% |
| **+10¢ (15¢ stop)** | 48557 | 48487 | 70 (37) | 0 | $-18388.24 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 21:55 | +10 stop | SOL | UP | 0.32 | 0.56 | 2.06 |
| 10-29 21:55 | +10 | SOL | UP | 0.33 | 0.56 | 1.98 |
| 10-29 21:55 | +5 | SOL | UP | 0.33 | 0.56 | 1.98 |
| 10-29 21:55 | +10 stop | XRP | UP | 0.53 | 0.72 | 1.57 |
| 10-29 21:55 | +5 | XRP | UP | 0.54 | 0.72 | 1.47 |
| 10-29 21:55 | +10 stop | ETH | UP | 0.61 | 0.31 | -3.32 |
| 10-29 21:55 | +10 | ETH | UP | 0.60 | open |  |
| 10-29 21:55 | +10 stop | ZEC | DOWN | 0.63 | 0.81 | 1.54 |
| 10-29 21:55 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-29 21:55 | +15 | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 10-29 21:55 | +10 | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 10-29 21:55 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-29 21:55 | +10 stop | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 10-29 21:54 | +10 stop | HYPE | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 21:54 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 10-29 21:54 | +15 | HYPE | DOWN | 0.61 | 0.83 | 1.90 |
| 10-29 21:54 | +10 | HYPE | DOWN | 0.61 | 0.83 | 1.90 |
| 10-29 21:54 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.34 |
| 10-29 21:54 | +5 | XRP | UP | 0.52 | 0.65 | 0.96 |
| 10-29 21:54 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-29 21:53 | +10 stop | XRP | UP | 0.68 | 0.43 | -2.84 |
| 10-29 21:53 | +20 | XRP | UP | 0.68 | open |  |
| 10-29 21:53 | +15 | XRP | UP | 0.68 | open |  |
| 10-29 21:53 | +10 | XRP | UP | 0.68 | open |  |
| 10-29 21:53 | +5 | XRP | UP | 0.68 | 0.76 | 0.51 |
| 10-29 21:52 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.90 |
| 10-29 21:52 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-29 21:52 | +15 | SOL | DOWN | 0.60 | 0.80 | 1.67 |
| 10-29 21:52 | +10 | SOL | DOWN | 0.61 | 0.73 | 0.90 |
| 10-29 21:52 | +5 | SOL | DOWN | 0.61 | 0.73 | 0.90 |
| 10-29 21:52 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-29 21:51 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-29 21:51 | +5 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 21:51 | +10 stop | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-29 21:51 | +10 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 10-29 21:51 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.48 |
| 10-29 21:50 | +10 stop | BTC | UP | 0.62 | 0.41 | -2.44 |
| 10-29 21:49 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 10-29 21:49 | +10 stop | DOGE | UP | 0.55 | 0.37 | -2.15 |
| 10-29 21:49 | +10 stop | BTC | DOWN | 0.52 | 0.37 | -1.85 |
