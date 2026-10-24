# Range-Scalp Bot

*Updated Sat Oct 24 05:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31483 | 27440 | 4043 (40) | 0 | $-9061.64 | -4.6% |
| **+10¢** | 23546 | 18877 | 4669 (58) | 0 | $-8045.08 | -5.4% |
| **+15¢** | 19715 | 14697 | 5018 (81) | 0 | $-7172.48 | -5.8% |
| **+20¢** | 17467 | 12212 | 5255 (103) | 0 | $-6379.04 | -5.8% |
| **+10¢ (15¢ stop)** | 38640 | 38581 | 59 (32) | 0 | $-14766.86 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 05:08 | +10 stop | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-24 05:08 | +10 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-24 05:08 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-24 05:04 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-24 05:01 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-24 05:01 | +20 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-24 05:01 | +15 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 10-24 05:01 | +10 | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-24 05:01 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-24 05:01 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.07 |
| 10-24 05:01 | +20 | NEAR | DOWN | 0.66 | 0.86 | 1.80 |
| 10-24 05:01 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 05:01 | +10 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 05:01 | +5 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 05:00 | +10 stop | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 05:00 | +20 | ZEC | DOWN | 0.64 | 0.87 | 2.05 |
| 10-24 05:00 | +15 | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-24 05:00 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 05:00 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-24 05:00 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-24 05:00 | +20 | DOGE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-24 05:00 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-24 05:00 | +10 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-24 05:00 | +5 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-24 05:00 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 05:00 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-24 05:00 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-24 05:00 | +10 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 05:00 | +5 | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-24 05:00 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-24 05:00 | +20 | HYPE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-24 05:00 | +15 | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-24 05:00 | +10 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-24 05:00 | +5 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 10-24 04:58 | +10 stop | BTC | UP | 0.54 | 0.73 | 1.54 |
| 10-24 04:57 | +5 | DOGE | UP | 0.54 | 0.66 | 0.86 |
| 10-24 04:56 | +10 stop | ZEC | UP | 0.58 | 0.40 | -2.15 |
| 10-24 04:55 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-24 04:55 | +20 | HYPE | UP | 0.64 | no | -6.57 |
| 10-24 04:55 | +15 | HYPE | UP | 0.64 | no | -6.57 |
