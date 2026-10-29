# Range-Scalp Bot

*Updated Thu Oct 29 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39592 | 34568 | 5024 (50) | 2 | $-10972.83 | -4.4% |
| **+10¢** | 29506 | 23700 | 5806 (73) | 7 | $-9712.78 | -5.2% |
| **+15¢** | 24669 | 18425 | 6244 (100) | 7 | $-8704.84 | -5.6% |
| **+20¢** | 21889 | 15349 | 6540 (129) | 8 | $-7579.45 | -5.5% |
| **+10¢ (15¢ stop)** | 48357 | 48287 | 70 (37) | 0 | $-18349.07 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 18:26 | +5 | BTC | UP | 0.33 | 0.56 | 1.96 |
| 10-29 18:24 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 10-29 18:24 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 10-29 18:23 | +10 stop | BTC | UP | 0.58 | 0.29 | -3.23 |
| 10-29 18:23 | +20 | BTC | UP | 0.58 | open |  |
| 10-29 18:23 | +15 | BTC | UP | 0.58 | open |  |
| 10-29 18:23 | +10 | BTC | UP | 0.58 | open |  |
| 10-29 18:23 | +5 | BTC | UP | 0.58 | 0.67 | 0.56 |
| 10-29 18:23 | +10 stop | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 18:23 | +10 stop | DOGE | UP | 0.50 | 0.67 | 1.36 |
| 10-29 18:23 | +20 | DOGE | UP | 0.50 | open |  |
| 10-29 18:23 | +15 | DOGE | UP | 0.50 | 0.67 | 1.36 |
| 10-29 18:23 | +10 | DOGE | UP | 0.50 | 0.67 | 1.36 |
| 10-29 18:23 | +5 | DOGE | UP | 0.50 | 0.67 | 1.36 |
| 10-29 18:23 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-29 18:23 | +10 stop | ETH | UP | 0.61 | 0.45 | -1.95 |
| 10-29 18:23 | +20 | ETH | UP | 0.61 | open |  |
| 10-29 18:23 | +15 | ETH | UP | 0.61 | open |  |
| 10-29 18:23 | +10 | ETH | UP | 0.61 | open |  |
| 10-29 18:23 | +5 | ETH | UP | 0.61 | open |  |
| 10-29 18:23 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-29 18:23 | +10 stop | BNB | UP | 0.67 | 0.48 | -2.24 |
| 10-29 18:23 | +20 | BNB | UP | 0.67 | open |  |
| 10-29 18:23 | +15 | BNB | UP | 0.67 | open |  |
| 10-29 18:23 | +10 | BNB | UP | 0.67 | open |  |
| 10-29 18:23 | +5 | BNB | UP | 0.67 | open |  |
| 10-29 18:22 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-29 18:22 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-29 18:22 | +10 stop | SOL | UP | 0.57 | 0.31 | -2.92 |
| 10-29 18:22 | +20 | SOL | UP | 0.56 | open |  |
| 10-29 18:22 | +15 | SOL | UP | 0.56 | open |  |
| 10-29 18:22 | +10 | SOL | UP | 0.56 | open |  |
| 10-29 18:22 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 10-29 18:22 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-29 18:22 | +20 | NEAR | UP | 0.58 | open |  |
| 10-29 18:22 | +15 | NEAR | UP | 0.58 | open |  |
| 10-29 18:22 | +10 | NEAR | UP | 0.58 | open |  |
| 10-29 18:22 | +10 stop | XRP | UP | 0.56 | 0.36 | -2.35 |
| 10-29 18:22 | +20 | XRP | UP | 0.52 | open |  |
| 10-29 18:22 | +15 | XRP | UP | 0.52 | open |  |
