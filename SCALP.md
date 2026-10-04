# Range-Scalp Bot

*Updated Sun Oct 04 14:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2397 | 2069 | 328 (3) | 4 | $-788.99 | -5.2% |
| **+10¢** | 1869 | 1503 | 366 (4) | 5 | $-599.19 | -5.1% |
| **+15¢** | 1569 | 1182 | 387 (5) | 6 | $-493.84 | -5.0% |
| **+20¢** | 1391 | 985 | 406 (9) | 6 | $-412.30 | -4.7% |
| **+10¢ (15¢ stop)** | 2962 | 2961 | 1 (1) | 2 | $-1105.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 14:51 | +10 stop | ZEC | UP | 0.33 | 0.52 | 1.61 |
| 10-04 14:50 | +10 stop | BTC | UP | 0.60 | 0.79 | 1.61 |
| 10-04 14:50 | +10 stop | ZEC | DOWN | 0.60 | 0.41 | -2.22 |
| 10-04 14:50 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-04 14:50 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:50 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:50 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-04 14:50 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-04 14:49 | +5 | BTC | DOWN | 0.51 | open |  |
| 10-04 14:48 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 10-04 14:48 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 10-04 14:48 | +10 stop | BTC | DOWN | 0.67 | 0.50 | -2.04 |
| 10-04 14:47 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 10-04 14:47 | +10 stop | SOL | UP | 0.61 | 0.75 | 1.09 |
| 10-04 14:47 | +20 | SOL | UP | 0.61 | 0.82 | 1.82 |
| 10-04 14:47 | +15 | SOL | UP | 0.61 | 0.78 | 1.40 |
| 10-04 14:47 | +10 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 10-04 14:47 | +5 | SOL | UP | 0.61 | 0.69 | 0.48 |
| 10-04 14:47 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.91 |
| 10-04 14:47 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-04 14:47 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-04 14:47 | +10 | BNB | DOWN | 0.64 | 0.76 | 0.86 |
| 10-04 14:47 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.20 |
| 10-04 14:46 | +10 stop | BTC | DOWN | 0.64 | 0.45 | -2.25 |
| 10-04 14:46 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-04 14:46 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-04 14:46 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-04 14:46 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-04 14:46 | +10 stop | XRP | UP | 0.52 | 0.64 | 0.86 |
| 10-04 14:46 | +20 | XRP | UP | 0.52 | 0.75 | 1.99 |
| 10-04 14:46 | +15 | XRP | UP | 0.52 | 0.75 | 1.99 |
| 10-04 14:46 | +10 | XRP | UP | 0.52 | 0.64 | 0.86 |
| 10-04 14:46 | +5 | XRP | UP | 0.51 | 0.64 | 0.95 |
| 10-04 14:46 | +10 stop | ZEC | UP | 0.62 | 0.44 | -2.12 |
| 10-04 14:46 | +20 | ZEC | UP | 0.62 | open |  |
| 10-04 14:46 | +15 | ZEC | UP | 0.62 | open |  |
| 10-04 14:46 | +10 | ZEC | UP | 0.59 | open |  |
| 10-04 14:46 | +5 | ZEC | UP | 0.59 | open |  |
| 10-04 14:46 | +10 stop | NEAR | UP | 0.59 | 0.40 | -2.24 |
| 10-04 14:46 | +20 | NEAR | UP | 0.59 | open |  |
