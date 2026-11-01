# Range-Scalp Bot

*Updated Sun Nov 01 03:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43172 | 37630 | 5542 (62) | 1 | $-12289.18 | -4.5% |
| **+10¢** | 32195 | 25791 | 6404 (84) | 1 | $-11015.16 | -5.4% |
| **+15¢** | 26938 | 20037 | 6901 (112) | 1 | $-10074.58 | -6.0% |
| **+20¢** | 23921 | 16691 | 7230 (146) | 2 | $-8908.22 | -5.9% |
| **+10¢ (15¢ stop)** | 52640 | 52557 | 83 (48) | 1 | $-19910.77 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 03:50 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-01 03:46 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.79 |
| 11-01 03:46 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-01 03:46 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.53 |
| 11-01 03:46 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.79 |
| 11-01 03:46 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.33 |
| 11-01 03:46 | +10 stop | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-01 03:46 | +20 | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-01 03:46 | +15 | BTC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-01 03:46 | +10 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-01 03:46 | +5 | BTC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-01 03:46 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 11-01 03:46 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-01 03:46 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-01 03:46 | +10 | NEAR | DOWN | 0.68 | open |  |
| 11-01 03:46 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-01 03:46 | +10 stop | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-01 03:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 11-01 03:46 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-01 03:46 | +10 | ZEC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-01 03:46 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-01 03:46 | +10 stop | BNB | DOWN | 0.65 | 0.79 | 1.16 |
| 11-01 03:46 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.79 |
| 11-01 03:46 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.26 |
| 11-01 03:46 | +10 | BNB | DOWN | 0.65 | 0.79 | 1.16 |
| 11-01 03:46 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.23 |
| 11-01 03:37 | +5 | ETH | DOWN | 0.63 | yes | -6.47 |
| 11-01 03:36 | +10 stop | ETH | DOWN | 0.60 | 0.41 | -2.24 |
| 11-01 03:36 | +20 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-01 03:36 | +15 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-01 03:36 | +10 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-01 03:36 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 11-01 03:35 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-01 03:34 | +5 | ETH | UP | 0.47 | 0.54 | 0.34 |
| 11-01 03:34 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
| 11-01 03:34 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-01 03:34 | +15 | BNB | UP | 0.63 | 0.82 | 1.62 |
| 11-01 03:34 | +10 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 11-01 03:34 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 11-01 03:33 | +5 | DOGE | UP | 0.68 | 0.76 | 0.51 |
