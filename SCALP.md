# Range-Scalp Bot

*Updated Thu Oct 29 17:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39508 | 34496 | 5012 (50) | 3 | $-10938.34 | -4.4% |
| **+10¢** | 29453 | 23660 | 5793 (73) | 3 | $-9681.63 | -5.2% |
| **+15¢** | 24628 | 18402 | 6226 (100) | 4 | $-8637.89 | -5.6% |
| **+20¢** | 21853 | 15331 | 6522 (129) | 3 | $-7509.82 | -5.5% |
| **+10¢ (15¢ stop)** | 48265 | 48195 | 70 (37) | 1 | $-18316.94 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 17:28 | +10 stop | ZEC | DOWN | 0.57 | open |  |
| 10-29 17:28 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-29 17:28 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-29 17:28 | +10 | ZEC | DOWN | 0.56 | open |  |
| 10-29 17:28 | +5 | ZEC | DOWN | 0.56 | open |  |
| 10-29 17:27 | +10 stop | XRP | UP | 0.70 | 0.45 | -2.83 |
| 10-29 17:26 | +10 stop | XRP | UP | 0.67 | 0.41 | -2.93 |
| 10-29 17:25 | +10 stop | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-29 17:25 | +15 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-29 17:25 | +10 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 10-29 17:25 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-29 17:25 | +10 stop | BTC | UP | 0.67 | 0.81 | 1.13 |
| 10-29 17:25 | +10 stop | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-29 17:25 | +10 stop | XRP | DOWN | 0.45 | 0.56 | 0.74 |
| 10-29 17:24 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-29 17:24 | +10 stop | SOL | UP | 0.56 | 0.30 | -2.93 |
| 10-29 17:22 | +10 stop | DOGE | UP | 0.63 | 0.43 | -2.35 |
| 10-29 17:22 | +10 stop | ZEC | UP | 0.64 | 0.47 | -2.05 |
| 10-29 17:22 | +10 stop | NEAR | DOWN | 0.66 | 0.76 | 0.72 |
| 10-29 17:22 | +20 | NEAR | DOWN | 0.66 | 0.88 | 1.97 |
| 10-29 17:22 | +15 | NEAR | DOWN | 0.66 | 0.88 | 1.97 |
| 10-29 17:22 | +10 | NEAR | DOWN | 0.66 | 0.76 | 0.72 |
| 10-29 17:22 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.51 |
| 10-29 17:22 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-29 17:22 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-29 17:21 | +10 stop | XRP | UP | 0.67 | 0.52 | -1.84 |
| 10-29 17:21 | +10 stop | BNB | DOWN | 0.62 | 0.43 | -2.25 |
| 10-29 17:21 | +15 | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 10-29 17:21 | +10 | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 10-29 17:21 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-29 17:21 | +10 stop | BTC | UP | 0.69 | 0.49 | -2.33 |
| 10-29 17:21 | +10 stop | ZEC | DOWN | 0.62 | 0.42 | -2.35 |
| 10-29 17:21 | +10 | ZEC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-29 17:21 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 10-29 17:20 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-29 17:20 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 10-29 17:20 | +10 stop | BTC | DOWN | 0.56 | 0.41 | -1.85 |
| 10-29 17:20 | +10 stop | SOL | DOWN | 0.63 | 0.47 | -1.95 |
| 10-29 17:20 | +10 stop | XRP | DOWN | 0.64 | 0.41 | -2.64 |
| 10-29 17:19 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
