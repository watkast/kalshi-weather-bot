# Range-Scalp Bot

*Updated Sun Nov 15 10:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60649 | 52908 | 7741 (112) | 4 | $-16437.95 | -4.3% |
| **+10¢** | 45305 | 36229 | 9076 (150) | 4 | $-15525.55 | -5.5% |
| **+15¢** | 37948 | 28156 | 9792 (188) | 5 | $-14218.86 | -6.0% |
| **+20¢** | 33824 | 23553 | 10271 (240) | 5 | $-12513.78 | -5.9% |
| **+10¢ (15¢ stop)** | 73819 | 73668 | 151 (89) | 0 | $-27168.53 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 10:58 | +5 | BNB | UP | 0.52 | 0.63 | 0.75 |
| 11-15 10:57 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.76 |
| 11-15 10:57 | +10 stop | BNB | DOWN | 0.47 | 0.57 | 0.64 |
| 11-15 10:57 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-15 10:55 | +10 stop | BNB | UP | 0.56 | 0.31 | -2.83 |
| 11-15 10:55 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 11-15 10:53 | +10 stop | XRP | DOWN | 0.63 | 0.45 | -2.15 |
| 11-15 10:53 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 11-15 10:53 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-15 10:53 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-15 10:53 | +10 stop | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 11-15 10:52 | +10 stop | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-15 10:52 | +10 stop | ETH | UP | 0.56 | 0.69 | 0.97 |
| 11-15 10:52 | +10 stop | BNB | DOWN | 0.64 | 0.43 | -2.45 |
| 11-15 10:52 | +20 | BNB | DOWN | 0.64 | open |  |
| 11-15 10:52 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-15 10:51 | +10 stop | DOGE | DOWN | 0.66 | 0.42 | -2.74 |
| 11-15 10:51 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-15 10:51 | +10 | DOGE | DOWN | 0.65 | open |  |
| 11-15 10:51 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-15 10:51 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 10:51 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-15 10:51 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 10:51 | +5 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-15 10:51 | +10 stop | XRP | DOWN | 0.66 | 0.49 | -2.04 |
| 11-15 10:50 | +10 stop | ETH | DOWN | 0.57 | 0.42 | -1.86 |
| 11-15 10:50 | +10 stop | BTC | DOWN | 0.71 | 0.51 | -2.33 |
| 11-15 10:50 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-15 10:49 | +5 | DOGE | DOWN | 0.62 | 0.75 | 0.99 |
| 11-15 10:49 | +10 stop | XRP | UP | 0.53 | 0.35 | -2.14 |
| 11-15 10:49 | +10 stop | NEAR | UP | 0.52 | 0.63 | 0.75 |
| 11-15 10:48 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-15 10:48 | +5 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-15 10:48 | +10 stop | XRP | UP | 0.67 | 0.52 | -1.84 |
| 11-15 10:48 | +10 | XRP | UP | 0.67 | 0.81 | 1.13 |
| 11-15 10:48 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 11-15 10:47 | +5 | BTC | UP | 0.63 | open |  |
| 11-15 10:47 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 11-15 10:47 | +10 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 11-15 10:47 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
