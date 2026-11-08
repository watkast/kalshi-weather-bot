# Range-Scalp Bot

*Updated Sun Nov 08 01:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51789 | 45159 | 6630 (80) | 4 | $-14348.38 | -4.4% |
| **+10¢** | 38657 | 30927 | 7730 (106) | 5 | $-13340.21 | -5.5% |
| **+15¢** | 32369 | 24038 | 8331 (135) | 7 | $-12230.24 | -6.0% |
| **+20¢** | 28796 | 20062 | 8734 (180) | 7 | $-10765.03 | -6.0% |
| **+10¢ (15¢ stop)** | 63077 | 62974 | 103 (61) | 2 | $-23355.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 01:33 | +5 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:33 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:33 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-08 01:32 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 11-08 01:31 | +10 stop | BTC | UP | 0.67 | 0.52 | -1.84 |
| 11-08 01:31 | +20 | BTC | UP | 0.67 | open |  |
| 11-08 01:31 | +15 | BTC | UP | 0.67 | open |  |
| 11-08 01:31 | +10 | BTC | UP | 0.67 | open |  |
| 11-08 01:31 | +5 | BTC | UP | 0.67 | open |  |
| 11-08 01:31 | +10 stop | BNB | DOWN | 0.57 | 0.39 | -2.15 |
| 11-08 01:31 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-08 01:31 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-08 01:31 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-08 01:31 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-08 01:31 | +10 stop | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-08 01:31 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-08 01:31 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-08 01:31 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-08 01:31 | +20 | ETH | UP | 0.67 | open |  |
| 11-08 01:31 | +15 | ETH | UP | 0.67 | open |  |
| 11-08 01:31 | +10 | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-08 01:31 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-08 01:31 | +10 stop | ZEC | UP | 0.66 | open |  |
| 11-08 01:31 | +20 | ZEC | UP | 0.66 | open |  |
| 11-08 01:31 | +15 | ZEC | UP | 0.66 | open |  |
| 11-08 01:31 | +10 | ZEC | UP | 0.66 | open |  |
| 11-08 01:31 | +5 | ZEC | UP | 0.66 | open |  |
| 11-08 01:31 | +10 stop | HYPE | UP | 0.70 | open |  |
| 11-08 01:31 | +20 | HYPE | UP | 0.70 | open |  |
| 11-08 01:31 | +15 | HYPE | UP | 0.70 | open |  |
| 11-08 01:31 | +10 | HYPE | UP | 0.70 | open |  |
| 11-08 01:31 | +5 | HYPE | UP | 0.70 | 0.79 | 0.63 |
| 11-08 01:30 | +10 stop | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 11-08 01:30 | +20 | DOGE | DOWN | 0.51 | open |  |
| 11-08 01:30 | +15 | DOGE | DOWN | 0.51 | open |  |
| 11-08 01:30 | +10 | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 11-08 01:30 | +5 | DOGE | DOWN | 0.50 | 0.62 | 0.85 |
| 11-08 01:30 | +10 stop | XRP | DOWN | 0.54 | 0.30 | -2.73 |
| 11-08 01:30 | +20 | XRP | DOWN | 0.54 | open |  |
| 11-08 01:30 | +15 | XRP | DOWN | 0.54 | open |  |
