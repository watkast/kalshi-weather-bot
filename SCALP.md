# Range-Scalp Bot

*Updated Thu Nov 05 22:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48786 | 42519 | 6267 (74) | 3 | $-13814.31 | -4.5% |
| **+10¢** | 36412 | 29123 | 7289 (100) | 5 | $-12708.04 | -5.6% |
| **+15¢** | 30495 | 22645 | 7850 (129) | 5 | $-11594.05 | -6.1% |
| **+20¢** | 27093 | 18865 | 8228 (168) | 5 | $-10270.00 | -6.0% |
| **+10¢ (15¢ stop)** | 59439 | 59344 | 95 (57) | 5 | $-22003.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 22:17 | +10 stop | XRP | UP | 0.56 | open |  |
| 11-05 22:17 | +20 | XRP | UP | 0.56 | open |  |
| 11-05 22:17 | +15 | XRP | UP | 0.56 | open |  |
| 11-05 22:17 | +10 | XRP | UP | 0.56 | open |  |
| 11-05 22:17 | +5 | XRP | UP | 0.56 | open |  |
| 11-05 22:17 | +10 stop | HYPE | UP | 0.62 | open |  |
| 11-05 22:17 | +20 | HYPE | UP | 0.62 | open |  |
| 11-05 22:17 | +15 | HYPE | UP | 0.63 | open |  |
| 11-05 22:17 | +10 | HYPE | UP | 0.63 | open |  |
| 11-05 22:17 | +5 | HYPE | UP | 0.62 | open |  |
| 11-05 22:16 | +10 stop | BTC | DOWN | 0.56 | open |  |
| 11-05 22:16 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-05 22:16 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-05 22:16 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-05 22:16 | +5 | BTC | DOWN | 0.56 | 0.62 | 0.25 |
| 11-05 22:16 | +10 stop | ETH | DOWN | 0.61 | open |  |
| 11-05 22:16 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-05 22:16 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-05 22:16 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-05 22:16 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-05 22:16 | +10 stop | BNB | UP | 0.63 | open |  |
| 11-05 22:16 | +20 | BNB | UP | 0.63 | open |  |
| 11-05 22:16 | +15 | BNB | UP | 0.64 | open |  |
| 11-05 22:16 | +10 | BNB | UP | 0.64 | open |  |
| 11-05 22:16 | +5 | BNB | UP | 0.64 | 0.71 | 0.38 |
| 11-05 22:12 | +10 stop | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-05 22:12 | +20 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-05 22:12 | +15 | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-05 22:12 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 22:12 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 22:11 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-05 22:11 | +20 | ZEC | UP | 0.69 | 0.91 | 1.96 |
| 11-05 22:11 | +15 | ZEC | UP | 0.69 | 0.91 | 1.96 |
| 11-05 22:11 | +10 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-05 22:11 | +5 | ZEC | UP | 0.68 | 0.77 | 0.61 |
| 11-05 22:10 | +15 | NEAR | DOWN | 0.60 | yes | -6.17 |
| 11-05 22:09 | +10 stop | NEAR | DOWN | 0.61 | 0.30 | -3.42 |
| 11-05 22:09 | +10 | NEAR | DOWN | 0.61 | yes | -6.27 |
| 11-05 22:09 | +5 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 11-05 22:08 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
