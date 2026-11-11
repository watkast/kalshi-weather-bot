# Range-Scalp Bot

*Updated Wed Nov 11 13:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55890 | 48740 | 7150 (94) | 1 | $-15274.53 | -4.3% |
| **+10¢** | 41762 | 33423 | 8339 (124) | 1 | $-14209.28 | -5.4% |
| **+15¢** | 35021 | 26025 | 8996 (158) | 1 | $-12972.69 | -5.9% |
| **+20¢** | 31190 | 21752 | 9438 (208) | 2 | $-11353.73 | -5.8% |
| **+10¢ (15¢ stop)** | 68083 | 67962 | 121 (73) | 0 | $-25030.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 13:36 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-11 13:34 | +5 | BNB | UP | 0.60 | open |  |
| 11-11 13:34 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-11 13:34 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-11 13:34 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 13:34 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 13:34 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-11 13:34 | +10 stop | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 11-11 13:33 | +10 stop | BNB | UP | 0.62 | 0.39 | -2.63 |
| 11-11 13:33 | +20 | BNB | UP | 0.62 | open |  |
| 11-11 13:33 | +15 | BNB | UP | 0.62 | open |  |
| 11-11 13:33 | +10 | BNB | UP | 0.61 | open |  |
| 11-11 13:33 | +5 | BNB | UP | 0.61 | 0.67 | 0.27 |
| 11-11 13:33 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 13:33 | +10 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-11 13:33 | +10 stop | ZEC | DOWN | 0.54 | 0.71 | 1.37 |
| 11-11 13:33 | +20 | ZEC | DOWN | 0.54 | 0.76 | 1.89 |
| 11-11 13:33 | +15 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-11 13:33 | +10 | ZEC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-11 13:33 | +5 | ZEC | DOWN | 0.55 | 0.62 | 0.35 |
| 11-11 13:33 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-11 13:31 | +10 stop | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-11 13:31 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.89 |
| 11-11 13:31 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-11 13:31 | +10 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-11 13:31 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-11 13:31 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-11 13:31 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-11 13:31 | +15 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-11 13:31 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-11 13:31 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-11 13:31 | +10 stop | DOGE | DOWN | 0.69 | 0.51 | -2.13 |
| 11-11 13:31 | +20 | DOGE | DOWN | 0.69 | 0.92 | 2.05 |
| 11-11 13:31 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-11 13:31 | +10 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-11 13:31 | +5 | DOGE | DOWN | 0.68 | 0.77 | 0.61 |
| 11-11 13:31 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 11-11 13:30 | +10 stop | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-11 13:30 | +20 | NEAR | DOWN | 0.58 | 0.81 | 2.01 |
| 11-11 13:30 | +15 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
