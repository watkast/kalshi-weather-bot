# Range-Scalp Bot

*Updated Sat Oct 24 06:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31558 | 27507 | 4051 (40) | 3 | $-9073.81 | -4.6% |
| **+10¢** | 23599 | 18920 | 4679 (58) | 3 | $-8057.77 | -5.4% |
| **+15¢** | 19761 | 14730 | 5031 (81) | 3 | $-7200.81 | -5.8% |
| **+20¢** | 17508 | 12241 | 5267 (103) | 3 | $-6394.80 | -5.8% |
| **+10¢ (15¢ stop)** | 38731 | 38672 | 59 (32) | 3 | $-14782.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 06:15 | +10 stop | ETH | DOWN | 0.55 | open |  |
| 10-24 06:15 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-24 06:15 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-24 06:15 | +10 | ETH | DOWN | 0.55 | open |  |
| 10-24 06:15 | +5 | ETH | DOWN | 0.55 | open |  |
| 10-24 06:15 | +10 stop | BTC | DOWN | 0.52 | open |  |
| 10-24 06:15 | +20 | BTC | DOWN | 0.52 | open |  |
| 10-24 06:15 | +15 | BTC | DOWN | 0.52 | open |  |
| 10-24 06:15 | +10 | BTC | DOWN | 0.52 | open |  |
| 10-24 06:15 | +5 | BTC | DOWN | 0.52 | open |  |
| 10-24 06:15 | +10 stop | SOL | UP | 0.60 | open |  |
| 10-24 06:15 | +20 | SOL | UP | 0.60 | open |  |
| 10-24 06:15 | +15 | SOL | UP | 0.60 | open |  |
| 10-24 06:15 | +10 | SOL | UP | 0.60 | open |  |
| 10-24 06:15 | +5 | SOL | UP | 0.60 | open |  |
| 10-24 06:13 | +10 stop | DOGE | UP | 0.67 | 0.16 | -5.36 |
| 10-24 06:13 | +20 | DOGE | UP | 0.67 | no | -6.86 |
| 10-24 06:13 | +15 | DOGE | UP | 0.67 | no | -6.86 |
| 10-24 06:13 | +10 | DOGE | UP | 0.67 | no | -6.86 |
| 10-24 06:13 | +5 | DOGE | UP | 0.67 | no | -6.86 |
| 10-24 06:12 | +10 stop | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-24 06:12 | +20 | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-24 06:12 | +15 | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-24 06:12 | +10 | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-24 06:12 | +5 | SOL | DOWN | 0.52 | 0.73 | 1.78 |
| 10-24 06:11 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-24 06:11 | +20 | BTC | DOWN | 0.69 | yes | -7.05 |
| 10-24 06:11 | +15 | BTC | DOWN | 0.69 | yes | -7.05 |
| 10-24 06:11 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-24 06:11 | +5 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-24 06:10 | +10 stop | XRP | UP | 0.57 | 0.67 | 0.66 |
| 10-24 06:09 | +10 stop | ETH | DOWN | 0.51 | 0.64 | 0.95 |
| 10-24 06:09 | +10 stop | XRP | DOWN | 0.64 | 0.45 | -2.25 |
| 10-24 06:09 | +20 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-24 06:09 | +15 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-24 06:09 | +10 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-24 06:09 | +5 | XRP | DOWN | 0.64 | yes | -6.57 |
| 10-24 06:04 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-24 06:04 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-24 06:04 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
