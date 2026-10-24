# Range-Scalp Bot

*Updated Sat Oct 24 08:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31754 | 27687 | 4067 (40) | 4 | $-9066.98 | -4.5% |
| **+10¢** | 23745 | 19045 | 4700 (58) | 4 | $-8059.09 | -5.4% |
| **+15¢** | 19878 | 14826 | 5052 (81) | 4 | $-7181.30 | -5.8% |
| **+20¢** | 17611 | 12323 | 5288 (103) | 5 | $-6358.09 | -5.7% |
| **+10¢ (15¢ stop)** | 39011 | 38952 | 59 (32) | 2 | $-14943.69 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 08:36 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-24 08:36 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 10-24 08:36 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 08:35 | +10 stop | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 10-24 08:35 | +10 stop | XRP | UP | 0.45 | 0.56 | 0.74 |
| 10-24 08:35 | +20 | XRP | UP | 0.44 | open |  |
| 10-24 08:35 | +20 | SOL | UP | 0.64 | open |  |
| 10-24 08:35 | +15 | SOL | UP | 0.64 | open |  |
| 10-24 08:35 | +5 | SOL | UP | 0.64 | open |  |
| 10-24 08:34 | +10 stop | DOGE | UP | 0.58 | 0.35 | -2.64 |
| 10-24 08:34 | +20 | ZEC | UP | 0.68 | open |  |
| 10-24 08:34 | +15 | ZEC | UP | 0.68 | open |  |
| 10-24 08:34 | +5 | ZEC | UP | 0.68 | open |  |
| 10-24 08:34 | +10 stop | SOL | UP | 0.64 | 0.43 | -2.45 |
| 10-24 08:34 | +10 | SOL | UP | 0.64 | open |  |
| 10-24 08:34 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 10-24 08:33 | +10 stop | ZEC | UP | 0.68 | 0.41 | -3.03 |
| 10-24 08:33 | +10 | ZEC | UP | 0.68 | open |  |
| 10-24 08:33 | +10 stop | BNB | DOWN | 0.54 | 0.67 | 0.96 |
| 10-24 08:32 | +10 stop | BTC | UP | 0.58 | 0.34 | -2.74 |
| 10-24 08:32 | +20 | BTC | UP | 0.58 | open |  |
| 10-24 08:32 | +15 | BTC | UP | 0.58 | open |  |
| 10-24 08:32 | +10 | BTC | UP | 0.58 | open |  |
| 10-24 08:32 | +5 | BTC | UP | 0.58 | open |  |
| 10-24 08:32 | +10 stop | BNB | UP | 0.61 | 0.39 | -2.54 |
| 10-24 08:32 | +20 | BNB | UP | 0.61 | open |  |
| 10-24 08:32 | +15 | BNB | UP | 0.61 | open |  |
| 10-24 08:32 | +10 | BNB | UP | 0.61 | open |  |
| 10-24 08:32 | +5 | BNB | UP | 0.61 | open |  |
| 10-24 08:31 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.25 |
| 10-24 08:31 | +20 | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 10-24 08:31 | +15 | DOGE | DOWN | 0.56 | 0.77 | 1.79 |
| 10-24 08:31 | +10 | DOGE | DOWN | 0.57 | 0.77 | 1.69 |
| 10-24 08:31 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-24 08:31 | +10 stop | ETH | DOWN | 0.55 | 0.36 | -2.25 |
| 10-24 08:31 | +20 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-24 08:31 | +15 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-24 08:31 | +10 | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-24 08:31 | +5 | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-24 08:31 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
