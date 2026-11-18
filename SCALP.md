# Range-Scalp Bot

*Updated Wed Nov 18 19:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64374 | 56147 | 8227 (124) | 0 | $-17570.77 | -4.3% |
| **+10¢** | 48085 | 38463 | 9622 (165) | 0 | $-16394.55 | -5.4% |
| **+15¢** | 40315 | 29945 | 10370 (210) | 0 | $-14819.93 | -5.9% |
| **+20¢** | 35899 | 25015 | 10884 (265) | 0 | $-13101.96 | -5.8% |
| **+10¢ (15¢ stop)** | 78313 | 78149 | 164 (98) | 0 | $-28841.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 18:57 | +10 stop | ZEC | DOWN | 0.48 | 0.88 | 3.74 |
| 11-18 18:57 | +20 | ZEC | DOWN | 0.49 | 0.88 | 3.64 |
| 11-18 18:57 | +15 | ZEC | DOWN | 0.49 | 0.88 | 3.64 |
| 11-18 18:57 | +10 | ZEC | DOWN | 0.49 | 0.88 | 3.64 |
| 11-18 18:57 | +5 | ZEC | DOWN | 0.49 | 0.54 | 0.14 |
| 11-18 18:55 | +10 stop | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 11-18 18:55 | +15 | ZEC | DOWN | 0.61 | 0.79 | 1.51 |
| 11-18 18:55 | +10 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-18 18:55 | +5 | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-18 18:53 | +10 stop | NEAR | UP | 0.63 | 0.82 | 1.62 |
| 11-18 18:52 | +5 | DOGE | DOWN | 0.70 | yes | -7.15 |
| 11-18 18:52 | +10 | DOGE | DOWN | 0.69 | yes | -7.05 |
| 11-18 18:52 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-18 18:51 | +10 stop | DOGE | DOWN | 0.68 | 0.52 | -1.94 |
| 11-18 18:51 | +10 stop | XRP | DOWN | 0.71 | 0.83 | 0.95 |
| 11-18 18:51 | +10 stop | ZEC | UP | 0.49 | 0.21 | -3.10 |
| 11-18 18:49 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.35 |
| 11-18 18:49 | +10 stop | NEAR | UP | 0.71 | 0.83 | 0.95 |
| 11-18 18:49 | +5 | BTC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-18 18:49 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 11-18 18:49 | +15 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:49 | +10 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:49 | +5 | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-18 18:48 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-18 18:48 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 11-18 18:48 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-18 18:48 | +5 | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-18 18:48 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-18 18:48 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-18 18:47 | +10 stop | DOGE | UP | 0.53 | 0.63 | 0.65 |
| 11-18 18:47 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-18 18:47 | +20 | ZEC | DOWN | 0.63 | 0.90 | 2.46 |
| 11-18 18:47 | +15 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:47 | +10 | ZEC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:47 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-18 18:46 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-18 18:46 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 11-18 18:46 | +15 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 11-18 18:46 | +10 | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-18 18:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
