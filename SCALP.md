# Range-Scalp Bot

*Updated Thu Nov 19 04:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64727 | 56480 | 8247 (124) | 5 | $-17483.80 | -4.3% |
| **+10¢** | 48357 | 38710 | 9647 (165) | 6 | $-16278.77 | -5.4% |
| **+15¢** | 40552 | 30150 | 10402 (210) | 7 | $-14696.01 | -5.8% |
| **+20¢** | 36112 | 25189 | 10923 (265) | 7 | $-12998.59 | -5.7% |
| **+10¢ (15¢ stop)** | 78747 | 78583 | 164 (98) | 0 | $-28885.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 04:27 | +10 stop | NEAR | UP | 0.10 | 0.65 | 5.31 |
| 11-19 04:27 | +15 | NEAR | UP | 0.10 | 0.65 | 5.31 |
| 11-19 04:27 | +10 | NEAR | UP | 0.10 | 0.65 | 5.30 |
| 11-19 04:27 | +5 | NEAR | UP | 0.09 | 0.65 | 5.35 |
| 11-19 04:27 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.91 |
| 11-19 04:26 | +10 stop | ETH | DOWN | 0.60 | 0.85 | 2.24 |
| 11-19 04:26 | +10 stop | BTC | UP | 0.60 | 0.40 | -2.34 |
| 11-19 04:25 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 11-19 04:24 | +10 stop | ETH | UP | 0.66 | 0.39 | -3.03 |
| 11-19 04:24 | +10 stop | BNB | UP | 0.66 | 0.80 | 1.12 |
| 11-19 04:23 | +10 stop | BTC | UP | 0.59 | 0.72 | 0.98 |
| 11-19 04:22 | +10 stop | XRP | UP | 0.70 | 0.42 | -3.13 |
| 11-19 04:22 | +10 stop | NEAR | UP | 0.68 | 0.78 | 0.74 |
| 11-19 04:22 | +15 | NEAR | UP | 0.69 | 0.85 | 1.40 |
| 11-19 04:22 | +10 | NEAR | UP | 0.68 | 0.83 | 1.19 |
| 11-19 04:22 | +5 | NEAR | UP | 0.69 | 0.74 | 0.25 |
| 11-19 04:22 | +10 stop | BNB | UP | 0.71 | 0.55 | -1.93 |
| 11-19 04:22 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-19 04:21 | +10 stop | SOL | UP | 0.71 | 0.83 | 0.95 |
| 11-19 04:21 | +10 stop | DOGE | UP | 0.69 | 0.83 | 1.15 |
| 11-19 04:21 | +5 | DOGE | UP | 0.69 | 0.78 | 0.62 |
| 11-19 04:21 | +10 stop | HYPE | UP | 0.67 | 0.85 | 1.55 |
| 11-19 04:21 | +10 | HYPE | UP | 0.66 | 0.85 | 1.65 |
| 11-19 04:21 | +5 | HYPE | UP | 0.66 | 0.75 | 0.60 |
| 11-19 04:21 | +10 stop | XRP | DOWN | 0.70 | 0.55 | -1.83 |
| 11-19 04:21 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-19 04:21 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-19 04:21 | +5 | XRP | DOWN | 0.71 | open |  |
| 11-19 04:21 | +10 stop | ZEC | UP | 0.50 | 0.68 | 1.46 |
| 11-19 04:21 | +10 stop | BTC | UP | 0.57 | 0.72 | 1.17 |
| 11-19 04:21 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-19 04:20 | +10 stop | HYPE | DOWN | 0.49 | 0.63 | 1.05 |
| 11-19 04:20 | +10 | HYPE | DOWN | 0.51 | 0.63 | 0.88 |
| 11-19 04:20 | +5 | HYPE | DOWN | 0.51 | 0.63 | 0.88 |
| 11-19 04:20 | +5 | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 11-19 04:20 | +10 stop | ETH | DOWN | 0.67 | 0.45 | -2.54 |
| 11-19 04:20 | +10 | ETH | DOWN | 0.67 | 0.85 | 1.55 |
| 11-19 04:20 | +5 | ETH | DOWN | 0.68 | 0.85 | 1.45 |
| 11-19 04:20 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.27 |
| 11-19 04:20 | +5 | BTC | DOWN | 0.61 | open |  |
