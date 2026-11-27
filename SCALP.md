# Range-Scalp Bot

*Updated Fri Nov 27 19:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73999 | 64589 | 9410 (171) | 1 | $-19631.09 | -4.2% |
| **+10¢** | 55138 | 44147 | 10991 (216) | 0 | $-18255.21 | -5.3% |
| **+15¢** | 46169 | 34332 | 11837 (274) | 0 | $-16311.45 | -5.6% |
| **+20¢** | 41089 | 28621 | 12468 (341) | 0 | $-14723.99 | -5.7% |
| **+10¢ (15¢ stop)** | 90095 | 89876 | 219 (135) | 0 | $-33319.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 19:50 | +10 stop | HYPE | DOWN | 0.71 | 0.56 | -1.83 |
| 11-27 19:49 | +10 stop | ZEC | DOWN | 0.47 | 0.65 | 1.46 |
| 11-27 19:48 | +10 stop | HYPE | UP | 0.59 | 0.40 | -2.24 |
| 11-27 19:48 | +5 | HYPE | UP | 0.59 | open |  |
| 11-27 19:47 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 11-27 19:47 | +5 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-27 19:46 | +5 | HYPE | DOWN | 0.55 | 0.60 | 0.15 |
| 11-27 19:46 | +10 stop | BNB | DOWN | 0.69 | 0.54 | -1.83 |
| 11-27 19:46 | +20 | BNB | DOWN | 0.69 | 0.92 | 2.09 |
| 11-27 19:46 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-27 19:46 | +10 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-27 19:46 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-27 19:46 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-27 19:46 | +20 | ETH | DOWN | 0.68 | 0.95 | 2.47 |
| 11-27 19:46 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-27 19:46 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-27 19:46 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 11-27 19:46 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-27 19:46 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.81 |
| 11-27 19:46 | +15 | NEAR | DOWN | 0.71 | 0.88 | 1.47 |
| 11-27 19:46 | +10 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 19:46 | +5 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-27 19:46 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-27 19:46 | +20 | HYPE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-27 19:46 | +15 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-27 19:46 | +10 | HYPE | DOWN | 0.61 | 0.80 | 1.61 |
| 11-27 19:46 | +5 | HYPE | DOWN | 0.61 | 0.66 | 0.17 |
| 11-27 19:46 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 19:46 | +20 | XRP | DOWN | 0.70 | 0.92 | 1.98 |
| 11-27 19:46 | +15 | XRP | DOWN | 0.70 | 0.87 | 1.47 |
| 11-27 19:46 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-27 19:46 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-27 19:46 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-27 19:46 | +20 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-27 19:46 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-27 19:46 | +10 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-27 19:46 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-27 19:46 | +10 stop | ZEC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-27 19:46 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-27 19:46 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
