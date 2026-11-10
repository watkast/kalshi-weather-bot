# Range-Scalp Bot

*Updated Tue Nov 10 01:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54112 | 47204 | 6908 (89) | 0 | $-14732.30 | -4.3% |
| **+10¢** | 40419 | 32357 | 8062 (117) | 0 | $-13696.69 | -5.4% |
| **+15¢** | 33878 | 25189 | 8689 (149) | 0 | $-12459.55 | -5.9% |
| **+20¢** | 30164 | 21051 | 9113 (195) | 1 | $-10880.34 | -5.8% |
| **+10¢ (15¢ stop)** | 65918 | 65808 | 110 (66) | 0 | $-24405.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 01:00 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 01:00 | +20 | NEAR | UP | 0.65 | open |  |
| 11-10 01:00 | +15 | NEAR | UP | 0.65 | 0.82 | 1.43 |
| 11-10 01:00 | +10 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 01:00 | +5 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 11-10 00:56 | +10 stop | NEAR | DOWN | 0.68 | 0.86 | 1.55 |
| 11-10 00:56 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.85 |
| 11-10 00:55 | +10 stop | ZEC | UP | 0.61 | 0.26 | -3.81 |
| 11-10 00:54 | +10 stop | XRP | UP | 0.53 | 0.36 | -2.05 |
| 11-10 00:54 | +5 | XRP | UP | 0.53 | 0.81 | 2.51 |
| 11-10 00:54 | +10 stop | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +20 | DOGE | DOWN | 0.67 | 0.92 | 2.27 |
| 11-10 00:54 | +15 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +10 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-10 00:54 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 11-10 00:53 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-10 00:53 | +20 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +15 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +10 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:53 | +5 | NEAR | DOWN | 0.65 | 0.86 | 1.85 |
| 11-10 00:52 | +10 stop | HYPE | DOWN | 0.64 | 0.45 | -2.25 |
| 11-10 00:52 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 11-10 00:52 | +5 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-10 00:51 | +10 | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 00:51 | +10 stop | XRP | DOWN | 0.66 | 0.36 | -3.33 |
| 11-10 00:51 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 00:51 | +10 stop | ZEC | DOWN | 0.71 | 0.48 | -2.63 |
| 11-10 00:50 | +5 | XRP | UP | 0.54 | 0.63 | 0.55 |
| 11-10 00:50 | +10 stop | SOL | DOWN | 0.60 | 0.77 | 1.40 |
| 11-10 00:49 | +10 stop | ETH | UP | 0.54 | 0.34 | -2.34 |
| 11-10 00:49 | +10 | ETH | UP | 0.54 | 0.85 | 2.83 |
| 11-10 00:49 | +5 | ETH | UP | 0.54 | 0.59 | 0.15 |
| 11-10 00:49 | +10 stop | ZEC | UP | 0.64 | 0.49 | -1.85 |
| 11-10 00:49 | +5 | HYPE | UP | 0.71 | 0.79 | 0.53 |
| 11-10 00:49 | +10 stop | BNB | UP | 0.65 | 0.43 | -2.54 |
| 11-10 00:49 | +10 stop | SOL | UP | 0.57 | 0.41 | -1.95 |
| 11-10 00:49 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 11-10 00:48 | +10 stop | ZEC | DOWN | 0.50 | 0.60 | 0.65 |
| 11-10 00:48 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-10 00:48 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
