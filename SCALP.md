# Range-Scalp Bot

*Updated Sat Oct 24 09:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31792 | 27716 | 4076 (40) | 0 | $-9108.80 | -4.5% |
| **+10¢** | 23776 | 19066 | 4710 (58) | 2 | $-8102.01 | -5.4% |
| **+15¢** | 19901 | 14839 | 5062 (81) | 2 | $-7225.26 | -5.8% |
| **+20¢** | 17632 | 12332 | 5300 (103) | 2 | $-6411.86 | -5.8% |
| **+10¢ (15¢ stop)** | 39049 | 38990 | 59 (32) | 2 | $-14931.17 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 09:16 | +5 | SOL | UP | 0.48 | 0.57 | 0.54 |
| 10-24 09:15 | +10 stop | ZEC | UP | 0.58 | open |  |
| 10-24 09:15 | +20 | ZEC | UP | 0.58 | open |  |
| 10-24 09:15 | +15 | ZEC | UP | 0.58 | open |  |
| 10-24 09:15 | +10 | ZEC | UP | 0.58 | open |  |
| 10-24 09:15 | +5 | ZEC | UP | 0.58 | 0.65 | 0.36 |
| 10-24 09:15 | +10 stop | SOL | UP | 0.60 | open |  |
| 10-24 09:15 | +20 | SOL | UP | 0.60 | open |  |
| 10-24 09:15 | +15 | SOL | UP | 0.60 | open |  |
| 10-24 09:15 | +10 | SOL | UP | 0.60 | open |  |
| 10-24 09:15 | +5 | SOL | UP | 0.60 | 0.67 | 0.37 |
| 10-24 09:07 | +10 stop | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-24 09:07 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-24 09:07 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 09:07 | +5 | DOGE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-24 09:06 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-24 09:05 | +10 stop | DOGE | DOWN | 0.60 | 0.76 | 1.26 |
| 10-24 09:05 | +15 | DOGE | DOWN | 0.60 | 0.76 | 1.33 |
| 10-24 09:05 | +10 | DOGE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-24 09:05 | +5 | DOGE | DOWN | 0.59 | 0.68 | 0.57 |
| 10-24 09:04 | +10 stop | HYPE | DOWN | 0.65 | 0.48 | -2.04 |
| 10-24 09:04 | +10 | HYPE | DOWN | 0.64 | 0.78 | 1.06 |
| 10-24 09:04 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.44 |
| 10-24 09:02 | +10 stop | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 10-24 09:02 | +10 stop | XRP | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 09:01 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.30 |
| 10-24 09:01 | +10 | HYPE | DOWN | 0.68 | 0.80 | 0.88 |
| 10-24 09:01 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.47 |
| 10-24 09:01 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-24 09:01 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 10-24 09:01 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-24 09:01 | +20 | BTC | DOWN | 0.70 | 0.92 | 1.98 |
| 10-24 09:01 | +15 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-24 09:01 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-24 09:01 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-24 09:01 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 09:01 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-24 09:01 | +15 | ETH | DOWN | 0.68 | 0.86 | 1.55 |
| 10-24 09:01 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-24 09:01 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
