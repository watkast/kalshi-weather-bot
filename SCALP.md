# Range-Scalp Bot

*Updated Mon Oct 19 18:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24373 | 21203 | 3170 (31) | 2 | $-7209.54 | -4.7% |
| **+10¢** | 18322 | 14661 | 3661 (46) | 2 | $-6450.39 | -5.6% |
| **+15¢** | 15344 | 11404 | 3940 (69) | 2 | $-5816.64 | -6.0% |
| **+20¢** | 13578 | 9453 | 4125 (87) | 2 | $-5223.57 | -6.1% |
| **+10¢ (15¢ stop)** | 29979 | 29927 | 52 (30) | 2 | $-11385.77 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 18:03 | +10 stop | SOL | UP | 0.69 | open |  |
| 10-19 18:03 | +20 | SOL | UP | 0.69 | open |  |
| 10-19 18:03 | +15 | SOL | UP | 0.69 | open |  |
| 10-19 18:03 | +10 | SOL | UP | 0.69 | open |  |
| 10-19 18:03 | +5 | SOL | UP | 0.69 | open |  |
| 10-19 18:02 | +10 stop | HYPE | UP | 0.64 | open |  |
| 10-19 18:02 | +20 | HYPE | UP | 0.64 | open |  |
| 10-19 18:02 | +15 | HYPE | UP | 0.64 | open |  |
| 10-19 18:02 | +10 | HYPE | UP | 0.63 | open |  |
| 10-19 18:02 | +5 | HYPE | UP | 0.63 | open |  |
| 10-19 18:00 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-19 18:00 | +20 | BTC | UP | 0.64 | 0.88 | 2.15 |
| 10-19 18:00 | +15 | BTC | UP | 0.64 | 0.88 | 2.15 |
| 10-19 18:00 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-19 18:00 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-19 18:00 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-19 18:00 | +20 | DOGE | UP | 0.66 | 0.91 | 2.30 |
| 10-19 18:00 | +15 | DOGE | UP | 0.66 | 0.91 | 2.30 |
| 10-19 18:00 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-19 18:00 | +5 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-19 18:00 | +10 stop | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-19 18:00 | +20 | HYPE | UP | 0.46 | 0.72 | 2.27 |
| 10-19 18:00 | +15 | HYPE | UP | 0.46 | 0.72 | 2.27 |
| 10-19 18:00 | +10 | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-19 18:00 | +5 | HYPE | UP | 0.46 | 0.58 | 0.84 |
| 10-19 17:46 | +20 | HYPE | DOWN | 0.71 | 0.94 | 2.14 |
| 10-19 17:46 | +15 | HYPE | DOWN | 0.70 | 0.94 | 2.23 |
| 10-19 17:46 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.85 |
| 10-19 17:46 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.22 |
| 10-19 17:43 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.73 |
| 10-19 17:43 | +20 | XRP | UP | 0.68 | 0.99 | 2.93 |
| 10-19 17:43 | +15 | XRP | UP | 0.68 | 0.99 | 2.93 |
| 10-19 17:43 | +10 | XRP | UP | 0.68 | 0.78 | 0.73 |
| 10-19 17:43 | +5 | XRP | UP | 0.66 | 0.78 | 0.91 |
| 10-19 17:42 | +10 stop | SOL | DOWN | 0.66 | 0.23 | -4.54 |
| 10-19 17:42 | +10 | SOL | DOWN | 0.66 | yes | -6.71 |
| 10-19 17:42 | +5 | SOL | DOWN | 0.66 | yes | -6.71 |
| 10-19 17:41 | +5 | BNB | UP | 0.60 | 0.67 | 0.41 |
| 10-19 17:40 | +10 stop | BNB | UP | 0.51 | 0.67 | 1.26 |
| 10-19 17:40 | +5 | BNB | UP | 0.51 | 0.58 | 0.34 |
