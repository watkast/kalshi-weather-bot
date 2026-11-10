# Range-Scalp Bot

*Updated Tue Nov 10 18:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54876 | 47865 | 7011 (91) | 2 | $-14965.87 | -4.3% |
| **+10¢** | 41002 | 32823 | 8179 (121) | 2 | $-13880.00 | -5.4% |
| **+15¢** | 34373 | 25559 | 8814 (155) | 1 | $-12604.97 | -5.8% |
| **+20¢** | 30601 | 21353 | 9248 (204) | 2 | $-11028.97 | -5.7% |
| **+10¢ (15¢ stop)** | 66862 | 66748 | 114 (70) | 0 | $-24736.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 18:27 | +10 stop | ZEC | DOWN | 0.30 | 0.65 | 3.20 |
| 11-10 18:26 | +20 | NEAR | DOWN | 0.53 | open |  |
| 11-10 18:26 | +10 stop | NEAR | DOWN | 0.65 | 0.50 | -1.84 |
| 11-10 18:26 | +10 | NEAR | DOWN | 0.65 | open |  |
| 11-10 18:26 | +5 | NEAR | DOWN | 0.65 | open |  |
| 11-10 18:26 | +10 stop | BNB | DOWN | 0.58 | 0.26 | -3.52 |
| 11-10 18:26 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-10 18:26 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-10 18:26 | +10 stop | BTC | UP | 0.58 | 0.73 | 1.18 |
| 11-10 18:26 | +5 | BTC | UP | 0.58 | 0.73 | 1.18 |
| 11-10 18:25 | +10 stop | BNB | UP | 0.52 | 0.65 | 0.96 |
| 11-10 18:25 | +15 | BNB | UP | 0.52 | 0.73 | 1.78 |
| 11-10 18:25 | +10 | BNB | UP | 0.52 | 0.65 | 0.96 |
| 11-10 18:25 | +5 | BNB | UP | 0.52 | 0.65 | 0.96 |
| 11-10 18:25 | +5 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 11-10 18:24 | +5 | NEAR | UP | 0.66 | 0.74 | 0.50 |
| 11-10 18:24 | +10 stop | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-10 18:24 | +5 | BTC | UP | 0.59 | 0.64 | 0.16 |
| 11-10 18:23 | +10 stop | BNB | UP | 0.56 | 0.69 | 0.97 |
| 11-10 18:23 | +10 | BNB | UP | 0.56 | 0.69 | 0.97 |
| 11-10 18:22 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 11-10 18:22 | +15 | NEAR | UP | 0.62 | 0.84 | 1.93 |
| 11-10 18:22 | +10 | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 11-10 18:22 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 11-10 18:22 | +10 stop | ZEC | DOWN | 0.65 | 0.48 | -2.04 |
| 11-10 18:22 | +10 stop | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-10 18:22 | +20 | NEAR | DOWN | 0.39 | 0.61 | 1.86 |
| 11-10 18:22 | +15 | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-10 18:22 | +10 | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-10 18:22 | +5 | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-10 18:22 | +5 | BNB | UP | 0.64 | 0.69 | 0.18 |
| 11-10 18:22 | +10 stop | ETH | UP | 0.57 | 0.77 | 1.69 |
| 11-10 18:22 | +20 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 11-10 18:22 | +15 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-10 18:22 | +10 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-10 18:22 | +5 | ETH | UP | 0.55 | 0.77 | 1.89 |
| 11-10 18:21 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 11-10 18:21 | +20 | BNB | UP | 0.56 | 0.80 | 2.10 |
| 11-10 18:21 | +15 | BNB | UP | 0.56 | 0.71 | 1.17 |
| 11-10 18:21 | +10 | BNB | UP | 0.56 | 0.67 | 0.76 |
