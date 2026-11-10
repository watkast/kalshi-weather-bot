# Range-Scalp Bot

*Updated Tue Nov 10 00:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54081 | 47174 | 6907 (89) | 2 | $-14744.69 | -4.3% |
| **+10¢** | 40396 | 32337 | 8059 (117) | 3 | $-13705.14 | -5.4% |
| **+15¢** | 33858 | 25172 | 8686 (149) | 3 | $-12470.15 | -5.9% |
| **+20¢** | 30145 | 21035 | 9110 (195) | 3 | $-10899.28 | -5.8% |
| **+10¢ (15¢ stop)** | 65881 | 65771 | 110 (66) | 0 | $-24369.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 00:18 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 00:18 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-10 00:18 | +5 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-10 00:18 | +10 stop | ZEC | UP | 0.48 | 0.33 | -1.84 |
| 11-10 00:17 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-10 00:17 | +20 | DOGE | DOWN | 0.55 | 0.79 | 2.10 |
| 11-10 00:17 | +15 | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 11-10 00:17 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-10 00:17 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 11-10 00:17 | +10 stop | NEAR | UP | 0.53 | 0.31 | -2.53 |
| 11-10 00:17 | +20 | NEAR | UP | 0.53 | open |  |
| 11-10 00:17 | +15 | NEAR | UP | 0.53 | open |  |
| 11-10 00:17 | +10 | NEAR | UP | 0.53 | open |  |
| 11-10 00:17 | +5 | NEAR | UP | 0.53 | open |  |
| 11-10 00:16 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 00:16 | +20 | BNB | DOWN | 0.65 | 0.90 | 2.31 |
| 11-10 00:16 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 00:16 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 00:16 | +5 | BNB | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 00:16 | +10 stop | ZEC | UP | 0.71 | 0.53 | -2.13 |
| 11-10 00:16 | +10 | ZEC | UP | 0.71 | open |  |
| 11-10 00:16 | +5 | ZEC | UP | 0.70 | open |  |
| 11-10 00:16 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 11-10 00:16 | +20 | XRP | UP | 0.61 | open |  |
| 11-10 00:16 | +15 | XRP | UP | 0.60 | open |  |
| 11-10 00:16 | +10 | XRP | UP | 0.60 | open |  |
| 11-10 00:16 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-10 00:15 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-10 00:15 | +20 | BTC | DOWN | 0.69 | 0.90 | 1.91 |
| 11-10 00:15 | +15 | BTC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-10 00:15 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-10 00:15 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-10 00:15 | +10 stop | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 00:15 | +20 | HYPE | DOWN | 0.69 | 0.93 | 2.17 |
| 11-10 00:15 | +15 | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-10 00:15 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-10 00:15 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 00:15 | +10 stop | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 11-10 00:15 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 11-10 00:15 | +15 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
