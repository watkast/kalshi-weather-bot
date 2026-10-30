# Range-Scalp Bot

*Updated Fri Oct 30 12:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40761 | 35573 | 5188 (51) | 5 | $-11420.18 | -4.4% |
| **+10¢** | 30362 | 24361 | 6001 (74) | 6 | $-10199.44 | -5.3% |
| **+15¢** | 25381 | 18921 | 6460 (101) | 7 | $-9236.85 | -5.8% |
| **+20¢** | 22525 | 15755 | 6770 (131) | 9 | $-8157.32 | -5.8% |
| **+10¢ (15¢ stop)** | 49696 | 49626 | 70 (37) | 3 | $-18819.41 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 12:24 | +5 | BTC | DOWN | 0.56 | open |  |
| 10-30 12:24 | +5 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-30 12:24 | +10 | SOL | DOWN | 0.67 | open |  |
| 10-30 12:24 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-30 12:24 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 10-30 12:24 | +5 | BTC | DOWN | 0.47 | 0.62 | 1.15 |
| 10-30 12:23 | +10 stop | HYPE | DOWN | 0.70 | 0.45 | -2.83 |
| 10-30 12:23 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-30 12:23 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 10-30 12:23 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-30 12:23 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 10-30 12:22 | +10 stop | ZEC | DOWN | 0.51 | 0.31 | -2.29 |
| 10-30 12:22 | +10 | ZEC | DOWN | 0.49 | open |  |
| 10-30 12:22 | +5 | ZEC | DOWN | 0.49 | 0.54 | 0.14 |
| 10-30 12:21 | +10 stop | XRP | DOWN | 0.64 | 0.49 | -1.85 |
| 10-30 12:21 | +10 stop | NEAR | DOWN | 0.68 | 0.47 | -2.44 |
| 10-30 12:21 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 0.97 |
| 10-30 12:21 | +10 stop | ZEC | UP | 0.50 | 0.63 | 0.95 |
| 10-30 12:21 | +20 | ZEC | UP | 0.53 | open |  |
| 10-30 12:21 | +15 | ZEC | UP | 0.53 | open |  |
| 10-30 12:21 | +10 | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 10-30 12:21 | +5 | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-30 12:21 | +10 stop | SOL | DOWN | 0.68 | open |  |
| 10-30 12:21 | +10 stop | BNB | DOWN | 0.63 | open |  |
| 10-30 12:21 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 12:21 | +10 stop | ETH | DOWN | 0.66 | 0.84 | 1.51 |
| 10-30 12:21 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.57 |
| 10-30 12:21 | +10 stop | XRP | UP | 0.54 | 0.38 | -1.95 |
| 10-30 12:20 | +10 stop | NEAR | UP | 0.59 | 0.43 | -1.95 |
| 10-30 12:20 | +10 stop | BTC | UP | 0.51 | 0.65 | 1.06 |
| 10-30 12:20 | +10 stop | ETH | UP | 0.47 | 0.57 | 0.64 |
| 10-30 12:20 | +5 | ETH | UP | 0.47 | 0.57 | 0.64 |
| 10-30 12:19 | +5 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 10-30 12:19 | +10 stop | BNB | DOWN | 0.65 | 0.46 | -2.24 |
| 10-30 12:19 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-30 12:19 | +10 stop | XRP | DOWN | 0.47 | 0.28 | -2.23 |
| 10-30 12:19 | +10 stop | SOL | DOWN | 0.53 | 0.25 | -3.12 |
| 10-30 12:19 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 10-30 12:19 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.07 |
| 10-30 12:19 | +15 | ZEC | UP | 0.58 | 0.82 | 2.11 |
