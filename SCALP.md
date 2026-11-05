# Range-Scalp Bot

*Updated Thu Nov 05 23:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48898 | 42608 | 6290 (74) | 5 | $-13905.60 | -4.5% |
| **+10¢** | 36497 | 29183 | 7314 (100) | 6 | $-12794.38 | -5.6% |
| **+15¢** | 30569 | 22692 | 7877 (129) | 7 | $-11685.69 | -6.1% |
| **+20¢** | 27162 | 18906 | 8256 (169) | 8 | $-10355.21 | -6.1% |
| **+10¢ (15¢ stop)** | 59629 | 59534 | 95 (57) | 0 | $-22109.03 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 23:58 | +10 stop | ETH | DOWN | 0.65 | 0.44 | -2.44 |
| 11-05 23:58 | +10 stop | BNB | DOWN | 0.70 | 0.38 | -3.52 |
| 11-05 23:58 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-05 23:57 | +10 stop | SOL | UP | 0.70 | 0.48 | -2.53 |
| 11-05 23:57 | +10 stop | ETH | UP | 0.71 | 0.36 | -3.82 |
| 11-05 23:57 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-05 23:56 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-05 23:55 | +10 stop | ZEC | DOWN | 0.64 | 0.82 | 1.52 |
| 11-05 23:53 | +10 stop | HYPE | DOWN | 0.58 | 0.42 | -1.96 |
| 11-05 23:52 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-05 23:52 | +10 stop | NEAR | DOWN | 0.61 | 0.79 | 1.51 |
| 11-05 23:52 | +10 stop | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 11-05 23:52 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-05 23:52 | +10 stop | HYPE | UP | 0.68 | 0.48 | -2.34 |
| 11-05 23:52 | +5 | HYPE | UP | 0.68 | open |  |
| 11-05 23:51 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 11-05 23:51 | +10 stop | BNB | DOWN | 0.49 | 0.59 | 0.65 |
| 11-05 23:50 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-05 23:49 | +10 stop | HYPE | UP | 0.57 | 0.71 | 1.07 |
| 11-05 23:49 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-05 23:49 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-05 23:49 | +5 | XRP | DOWN | 0.70 | 0.77 | 0.42 |
| 11-05 23:48 | +5 | HYPE | UP | 0.64 | 0.71 | 0.38 |
| 11-05 23:48 | +10 stop | ZEC | UP | 0.64 | 0.40 | -2.74 |
| 11-05 23:48 | +20 | ZEC | UP | 0.64 | open |  |
| 11-05 23:48 | +15 | ZEC | UP | 0.64 | open |  |
| 11-05 23:48 | +10 | ZEC | UP | 0.64 | open |  |
| 11-05 23:48 | +5 | ZEC | UP | 0.64 | open |  |
| 11-05 23:48 | +10 stop | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 11-05 23:48 | +10 stop | NEAR | UP | 0.62 | 0.46 | -1.95 |
| 11-05 23:48 | +10 | NEAR | UP | 0.62 | open |  |
| 11-05 23:47 | +5 | DOGE | UP | 0.62 | open |  |
| 11-05 23:47 | +5 | BTC | UP | 0.56 | 0.66 | 0.66 |
| 11-05 23:47 | +5 | NEAR | UP | 0.69 | open |  |
| 11-05 23:47 | +5 | DOGE | UP | 0.62 | 0.68 | 0.27 |
| 11-05 23:47 | +10 stop | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 23:47 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 11-05 23:47 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 23:47 | +10 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 23:47 | +5 | XRP | DOWN | 0.62 | 0.68 | 0.27 |
