# Range-Scalp Bot

*Updated Thu Oct 08 15:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7613 | 6598 | 1015 (13) | 0 | $-2366.69 | -4.9% |
| **+10¢** | 5775 | 4576 | 1199 (24) | 0 | $-2306.15 | -6.3% |
| **+15¢** | 4854 | 3592 | 1262 (32) | 0 | $-1889.09 | -6.2% |
| **+20¢** | 4338 | 3029 | 1309 (40) | 0 | $-1478.80 | -5.4% |
| **+10¢ (15¢ stop)** | 9228 | 9199 | 29 (18) | 0 | $-3362.56 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 15:01 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +20 | XRP | DOWN | 0.71 | 0.91 | 1.81 |
| 10-08 15:01 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-08 15:01 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-08 15:01 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +20 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 10-08 15:01 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-08 15:01 | +10 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +5 | DOGE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +10 stop | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 10-08 15:01 | +20 | BNB | DOWN | 0.60 | 0.84 | 2.13 |
| 10-08 15:01 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-08 15:01 | +10 | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 10-08 15:01 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-08 15:01 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 15:01 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-08 15:01 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-08 15:01 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 15:01 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-08 15:01 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +20 | HYPE | DOWN | 0.68 | 0.91 | 2.08 |
| 10-08 15:01 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-08 15:01 | +10 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +5 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-08 15:01 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-08 15:01 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 10-08 15:01 | +15 | ETH | DOWN | 0.65 | 0.83 | 1.54 |
| 10-08 15:01 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-08 15:01 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-08 14:57 | +10 stop | HYPE | DOWN | 0.57 | 0.28 | -3.23 |
| 10-08 14:57 | +10 stop | NEAR | UP | 0.54 | 0.77 | 1.99 |
| 10-08 14:56 | +10 stop | HYPE | UP | 0.68 | 0.39 | -3.20 |
| 10-08 14:55 | +10 stop | HYPE | DOWN | 0.65 | 0.44 | -2.44 |
| 10-08 14:55 | +15 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-08 14:55 | +10 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-08 14:55 | +5 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 10-08 14:55 | +10 stop | NEAR | UP | 0.59 | 0.70 | 0.78 |
| 10-08 14:55 | +10 stop | BTC | UP | 0.70 | 0.91 | 1.87 |
| 10-08 14:55 | +20 | BTC | UP | 0.70 | 0.91 | 1.87 |
