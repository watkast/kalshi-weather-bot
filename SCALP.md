# Range-Scalp Bot

*Updated Fri Oct 30 18:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41077 | 35855 | 5222 (53) | 1 | $-11452.26 | -4.4% |
| **+10¢** | 30608 | 24567 | 6041 (76) | 1 | $-10184.23 | -5.3% |
| **+15¢** | 25585 | 19076 | 6509 (103) | 3 | $-9244.90 | -5.8% |
| **+20¢** | 22710 | 15891 | 6819 (133) | 3 | $-8147.01 | -5.7% |
| **+10¢ (15¢ stop)** | 50079 | 50009 | 70 (37) | 2 | $-18941.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 18:01 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-30 18:01 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-30 18:01 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-30 18:01 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-30 18:01 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-30 18:01 | +10 stop | BNB | UP | 0.49 | open |  |
| 10-30 18:01 | +20 | BNB | UP | 0.50 | open |  |
| 10-30 18:01 | +15 | BNB | UP | 0.49 | open |  |
| 10-30 18:01 | +10 | BNB | UP | 0.47 | 0.58 | 0.74 |
| 10-30 18:01 | +5 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 10-30 18:01 | +10 stop | ETH | UP | 0.43 | 0.55 | 0.84 |
| 10-30 18:01 | +20 | ETH | UP | 0.43 | open |  |
| 10-30 18:01 | +15 | ETH | UP | 0.43 | open |  |
| 10-30 18:01 | +10 | ETH | UP | 0.44 | 0.55 | 0.74 |
| 10-30 18:01 | +5 | ETH | UP | 0.45 | 0.55 | 0.64 |
| 10-30 17:51 | +10 stop | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-30 17:51 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 17:50 | +10 stop | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 17:50 | +10 stop | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-30 17:50 | +20 | BNB | DOWN | 0.70 | 0.91 | 1.83 |
| 10-30 17:50 | +15 | BNB | DOWN | 0.70 | 0.91 | 1.83 |
| 10-30 17:50 | +10 | BNB | DOWN | 0.70 | 0.82 | 0.94 |
| 10-30 17:50 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.32 |
| 10-30 17:50 | +10 stop | HYPE | UP | 0.59 | 0.34 | -2.87 |
| 10-30 17:50 | +10 | HYPE | UP | 0.59 | no | -6.11 |
| 10-30 17:50 | +5 | HYPE | UP | 0.59 | no | -6.11 |
| 10-30 17:50 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.76 |
| 10-30 17:49 | +10 stop | BTC | UP | 0.67 | 0.41 | -2.93 |
| 10-30 17:49 | +5 | BTC | UP | 0.67 | no | -6.86 |
| 10-30 17:49 | +10 stop | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-30 17:49 | +10 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-30 17:49 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-30 17:49 | +5 | SOL | DOWN | 0.65 | 0.72 | 0.39 |
| 10-30 17:49 | +10 stop | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-30 17:49 | +5 | BTC | UP | 0.58 | 0.68 | 0.66 |
| 10-30 17:49 | +5 | ETH | UP | 0.56 | no | -5.78 |
| 10-30 17:48 | +5 | XRP | UP | 0.59 | no | -6.07 |
| 10-30 17:48 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 10-30 17:48 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-30 17:47 | +10 stop | BTC | UP | 0.54 | 0.66 | 0.86 |
