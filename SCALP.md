# Range-Scalp Bot

*Updated Thu Nov 19 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64483 | 56249 | 8234 (124) | 2 | $-17547.01 | -4.3% |
| **+10¢** | 48170 | 38540 | 9630 (165) | 4 | $-16360.29 | -5.4% |
| **+15¢** | 40391 | 30011 | 10380 (210) | 5 | $-14777.06 | -5.8% |
| **+20¢** | 35968 | 25071 | 10897 (265) | 5 | $-13072.08 | -5.8% |
| **+10¢ (15¢ stop)** | 78445 | 78281 | 164 (98) | 0 | $-28849.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 00:21 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 00:21 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-19 00:20 | +10 stop | HYPE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-19 00:20 | +5 | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
| 11-19 00:18 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-19 00:18 | +10 stop | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 11-19 00:18 | +10 stop | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-19 00:18 | +5 | NEAR | DOWN | 0.58 | 0.68 | 0.66 |
| 11-19 00:18 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-19 00:18 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-19 00:18 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-19 00:18 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 00:18 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-19 00:18 | +5 | NEAR | UP | 0.48 | 0.54 | 0.24 |
| 11-19 00:17 | +10 stop | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 00:17 | +20 | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 00:17 | +15 | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 00:17 | +10 | BTC | DOWN | 0.54 | 0.75 | 1.78 |
| 11-19 00:17 | +5 | BTC | DOWN | 0.54 | 0.62 | 0.45 |
| 11-19 00:17 | +10 stop | BNB | DOWN | 0.47 | 0.57 | 0.64 |
| 11-19 00:17 | +20 | BNB | DOWN | 0.47 | 0.70 | 1.97 |
| 11-19 00:17 | +15 | BNB | DOWN | 0.47 | 0.70 | 1.97 |
| 11-19 00:17 | +10 | BNB | DOWN | 0.47 | 0.57 | 0.64 |
| 11-19 00:17 | +5 | BNB | DOWN | 0.47 | 0.55 | 0.44 |
| 11-19 00:17 | +10 stop | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-19 00:17 | +20 | ZEC | DOWN | 0.56 | 0.79 | 2.00 |
| 11-19 00:17 | +15 | ZEC | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 00:17 | +10 | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-19 00:17 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.35 |
| 11-19 00:17 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-19 00:17 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.91 |
| 11-19 00:17 | +15 | XRP | DOWN | 0.66 | 0.82 | 1.38 |
| 11-19 00:17 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.76 |
| 11-19 00:17 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.76 |
| 11-19 00:16 | +10 stop | HYPE | UP | 0.65 | 0.46 | -2.24 |
| 11-19 00:16 | +20 | HYPE | UP | 0.65 | open |  |
| 11-19 00:16 | +15 | HYPE | UP | 0.65 | open |  |
| 11-19 00:16 | +10 | HYPE | UP | 0.65 | open |  |
| 11-19 00:16 | +5 | HYPE | UP | 0.65 | 0.71 | 0.29 |
| 11-19 00:16 | +15 | NEAR | UP | 0.59 | open |  |
