# Range-Scalp Bot

*Updated Thu Nov 05 22:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48831 | 42553 | 6278 (74) | 1 | $-13858.39 | -4.5% |
| **+10¢** | 36449 | 29150 | 7299 (100) | 1 | $-12735.40 | -5.6% |
| **+15¢** | 30530 | 22670 | 7860 (129) | 1 | $-11613.74 | -6.1% |
| **+20¢** | 27127 | 18888 | 8239 (168) | 1 | $-10290.65 | -6.0% |
| **+10¢ (15¢ stop)** | 59503 | 59408 | 95 (57) | 0 | $-22012.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 22:58 | +5 | ZEC | UP | 0.57 | open |  |
| 11-05 22:57 | +10 stop | SOL | DOWN | 0.70 | 0.96 | 2.41 |
| 11-05 22:57 | +20 | SOL | DOWN | 0.70 | 0.96 | 2.41 |
| 11-05 22:57 | +10 | SOL | DOWN | 0.70 | 0.96 | 2.41 |
| 11-05 22:57 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-05 22:56 | +15 | SOL | DOWN | 0.71 | 0.96 | 2.31 |
| 11-05 22:55 | +10 stop | ZEC | UP | 0.70 | 0.54 | -1.93 |
| 11-05 22:55 | +20 | ZEC | UP | 0.70 | open |  |
| 11-05 22:55 | +15 | ZEC | UP | 0.70 | open |  |
| 11-05 22:55 | +10 | ZEC | UP | 0.70 | open |  |
| 11-05 22:55 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 11-05 22:55 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 22:55 | +20 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-05 22:55 | +15 | BTC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-05 22:55 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 22:55 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 22:54 | +10 stop | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 11-05 22:54 | +20 | ZEC | UP | 0.47 | 0.72 | 2.17 |
| 11-05 22:54 | +15 | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 11-05 22:54 | +10 | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 11-05 22:54 | +5 | ZEC | UP | 0.47 | 0.66 | 1.56 |
| 11-05 22:53 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-05 22:53 | +20 | HYPE | DOWN | 0.67 | 0.88 | 1.86 |
| 11-05 22:53 | +15 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-05 22:53 | +10 | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-05 22:53 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-05 22:52 | +10 stop | DOGE | DOWN | 0.65 | 0.81 | 1.33 |
| 11-05 22:52 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-05 22:52 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-05 22:52 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-05 22:52 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 11-05 22:47 | +10 stop | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-05 22:47 | +20 | ETH | DOWN | 0.70 | 0.90 | 1.79 |
| 11-05 22:47 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-05 22:47 | +10 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 11-05 22:47 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-05 22:46 | +10 stop | XRP | DOWN | 0.55 | 0.86 | 2.83 |
| 11-05 22:46 | +20 | XRP | DOWN | 0.55 | 0.86 | 2.83 |
| 11-05 22:46 | +15 | XRP | DOWN | 0.55 | 0.86 | 2.83 |
| 11-05 22:46 | +10 | XRP | DOWN | 0.55 | 0.86 | 2.83 |
