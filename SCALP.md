# Range-Scalp Bot

*Updated Thu Nov 12 10:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56780 | 49490 | 7290 (101) | 1 | $-15675.16 | -4.4% |
| **+10¢** | 42432 | 33929 | 8503 (133) | 1 | $-14602.24 | -5.5% |
| **+15¢** | 35575 | 26422 | 9153 (167) | 2 | $-13243.32 | -5.9% |
| **+20¢** | 31688 | 22084 | 9604 (217) | 2 | $-11638.52 | -5.9% |
| **+10¢ (15¢ stop)** | 69234 | 69106 | 128 (78) | 1 | $-25608.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 10:31 | +10 stop | ETH | DOWN | 0.70 | 0.54 | -1.93 |
| 11-12 10:31 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +15 | ETH | DOWN | 0.71 | open |  |
| 11-12 10:31 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-12 10:31 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-12 10:31 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-12 10:31 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-12 10:31 | +10 | ZEC | DOWN | 0.59 | 0.70 | 0.78 |
| 11-12 10:31 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-12 06:31 | +10 stop | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +20 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +15 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +10 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +5 | NEAR | DOWN | 0.69 | no | 2.95 |
| 11-12 06:31 | +10 stop | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +15 | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +10 stop | ZEC | DOWN | 0.65 | no | 3.34 |
| 11-12 06:31 | +20 | ZEC | DOWN | 0.65 | no | 3.34 |
| 11-12 06:31 | +15 | ZEC | DOWN | 0.65 | no | 3.34 |
| 11-12 06:31 | +10 | ZEC | DOWN | 0.65 | no | 3.34 |
| 11-12 06:31 | +5 | ZEC | DOWN | 0.65 | no | 3.34 |
| 11-12 06:31 | +20 | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +10 | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +5 | XRP | DOWN | 0.71 | no | 2.75 |
| 11-12 06:31 | +10 stop | HYPE | DOWN | 0.61 | no | 3.73 |
| 11-12 06:31 | +20 | HYPE | DOWN | 0.61 | no | 3.73 |
| 11-12 06:31 | +15 | HYPE | DOWN | 0.61 | no | 3.73 |
| 11-12 06:31 | +10 | HYPE | DOWN | 0.61 | no | 3.73 |
| 11-12 06:31 | +5 | HYPE | DOWN | 0.61 | 0.67 | 0.27 |
| 11-12 06:31 | +10 stop | BNB | DOWN | 0.68 | no | 3.08 |
| 11-12 06:31 | +20 | BNB | DOWN | 0.68 | no | 3.08 |
| 11-12 06:31 | +15 | BNB | DOWN | 0.68 | no | 3.08 |
| 11-12 06:31 | +10 | BNB | DOWN | 0.68 | no | 3.08 |
| 11-12 06:31 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.24 |
| 11-12 06:29 | +10 stop | ZEC | DOWN | 0.06 | 0.60 | 5.23 |
| 11-12 06:28 | +10 stop | ZEC | UP | 0.64 | 0.39 | -2.84 |
| 11-12 06:28 | +10 stop | BTC | UP | 0.65 | 0.40 | -2.83 |
| 11-12 06:28 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-12 06:28 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
