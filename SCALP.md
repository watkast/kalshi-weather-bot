# Range-Scalp Bot

*Updated Wed Nov 18 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63479 | 55361 | 8118 (118) | 5 | $-17368.75 | -4.3% |
| **+10¢** | 47418 | 37918 | 9500 (159) | 5 | $-16283.57 | -5.5% |
| **+15¢** | 39754 | 29510 | 10244 (203) | 6 | $-14780.45 | -5.9% |
| **+20¢** | 35411 | 24661 | 10750 (258) | 7 | $-13050.12 | -5.9% |
| **+10¢ (15¢ stop)** | 77258 | 77100 | 158 (93) | 4 | $-28443.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 02:26 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-18 02:26 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-18 02:25 | +10 stop | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-18 02:25 | +20 | XRP | DOWN | 0.55 | open |  |
| 11-18 02:25 | +15 | XRP | DOWN | 0.55 | open |  |
| 11-18 02:25 | +10 | XRP | DOWN | 0.55 | 0.66 | 0.76 |
| 11-18 02:25 | +5 | XRP | DOWN | 0.56 | 0.66 | 0.71 |
| 11-18 02:25 | +5 | DOGE | UP | 0.63 | open |  |
| 11-18 02:25 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-18 02:25 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-18 02:25 | +5 | DOGE | UP | 0.60 | 0.69 | 0.60 |
| 11-18 02:24 | +10 stop | BNB | DOWN | 0.63 | open |  |
| 11-18 02:24 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-18 02:24 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-18 02:24 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-18 02:24 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-18 02:24 | +10 stop | SOL | UP | 0.69 | 0.84 | 1.25 |
| 11-18 02:24 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-18 02:24 | +10 stop | BTC | UP | 0.51 | 0.71 | 1.67 |
| 11-18 02:24 | +15 | BTC | UP | 0.51 | 0.71 | 1.67 |
| 11-18 02:24 | +10 | BTC | UP | 0.51 | 0.71 | 1.67 |
| 11-18 02:24 | +5 | BTC | UP | 0.51 | 0.58 | 0.34 |
| 11-18 02:24 | +10 stop | DOGE | DOWN | 0.57 | 0.38 | -2.25 |
| 11-18 02:24 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-18 02:24 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-18 02:24 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-18 02:24 | +10 stop | ETH | DOWN | 0.59 | 0.38 | -2.44 |
| 11-18 02:24 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-18 02:24 | +15 | ETH | DOWN | 0.59 | open |  |
| 11-18 02:24 | +10 | ETH | DOWN | 0.58 | open |  |
| 11-18 02:24 | +5 | ETH | DOWN | 0.56 | 0.61 | 0.15 |
| 11-18 02:24 | +10 stop | ZEC | DOWN | 0.58 | 0.27 | -3.42 |
| 11-18 02:24 | +10 | ZEC | DOWN | 0.60 | open |  |
| 11-18 02:24 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-18 02:24 | +10 stop | BTC | DOWN | 0.37 | 0.54 | 1.35 |
| 11-18 02:24 | +20 | BTC | DOWN | 0.37 | open |  |
| 11-18 02:24 | +15 | BTC | DOWN | 0.37 | 0.54 | 1.35 |
| 11-18 02:24 | +10 | BTC | DOWN | 0.37 | 0.54 | 1.35 |
| 11-18 02:24 | +5 | BTC | DOWN | 0.37 | 0.54 | 1.35 |
| 11-18 02:23 | +15 | SOL | DOWN | 0.58 | open |  |
