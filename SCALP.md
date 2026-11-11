# Range-Scalp Bot

*Updated Wed Nov 11 19:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56085 | 48910 | 7175 (94) | 0 | $-15331.57 | -4.3% |
| **+10¢** | 41908 | 33534 | 8374 (124) | 0 | $-14312.26 | -5.4% |
| **+15¢** | 35142 | 26115 | 9027 (158) | 0 | $-13021.60 | -5.9% |
| **+20¢** | 31302 | 21833 | 9469 (208) | 0 | $-11380.53 | -5.8% |
| **+10¢ (15¢ stop)** | 68326 | 68205 | 121 (73) | 0 | $-25142.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 19:02 | +10 stop | HYPE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-11 19:02 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-11 19:02 | +15 | HYPE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-11 19:02 | +10 | HYPE | DOWN | 0.64 | 0.82 | 1.52 |
| 11-11 19:02 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-11 19:02 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-11 19:01 | +10 stop | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 11-11 19:01 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-11 19:01 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 11-11 19:01 | +10 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 11-11 19:01 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.48 |
| 11-11 19:01 | +10 stop | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 19:01 | +20 | XRP | DOWN | 0.63 | 0.87 | 2.15 |
| 11-11 19:01 | +15 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 19:01 | +10 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 19:01 | +5 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 19:01 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-11 19:01 | +20 | DOGE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-11 19:01 | +15 | DOGE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-11 19:01 | +10 | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-11 19:01 | +5 | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-11 19:01 | +10 stop | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 11-11 19:01 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 11-11 19:01 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 11-11 19:01 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-11 19:01 | +5 | ETH | DOWN | 0.67 | 0.75 | 0.50 |
| 11-11 19:01 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 19:01 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-11 19:01 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-11 19:01 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 19:01 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 19:00 | +10 stop | NEAR | DOWN | 0.67 | 0.81 | 1.15 |
| 11-11 19:00 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.78 |
| 11-11 19:00 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.24 |
| 11-11 19:00 | +10 | NEAR | DOWN | 0.66 | 0.81 | 1.24 |
| 11-11 19:00 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.20 |
| 11-11 19:00 | +10 stop | BNB | DOWN | 0.69 | 0.83 | 1.11 |
| 11-11 19:00 | +20 | BNB | DOWN | 0.69 | 0.92 | 2.07 |
| 11-11 19:00 | +15 | BNB | DOWN | 0.70 | 0.87 | 1.51 |
| 11-11 19:00 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.09 |
