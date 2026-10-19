# Range-Scalp Bot

*Updated Mon Oct 19 14:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24096 | 20952 | 3144 (31) | 0 | $-7185.70 | -4.7% |
| **+10¢** | 18129 | 14502 | 3627 (46) | 0 | $-6413.52 | -5.6% |
| **+15¢** | 15193 | 11288 | 3905 (69) | 1 | $-5791.75 | -6.1% |
| **+20¢** | 13447 | 9361 | 4086 (87) | 1 | $-5173.39 | -6.1% |
| **+10¢ (15¢ stop)** | 29661 | 29609 | 52 (30) | 0 | $-11254.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 14:01 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 14:01 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-19 14:01 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-19 14:01 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 14:01 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-19 13:52 | +10 stop | NEAR | UP | 0.53 | 0.29 | -2.73 |
| 10-19 13:51 | +10 stop | HYPE | DOWN | 0.58 | 0.72 | 1.07 |
| 10-19 13:50 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-19 13:50 | +10 stop | BNB | UP | 0.50 | 0.30 | -2.33 |
| 10-19 13:50 | +10 stop | SOL | DOWN | 0.56 | 0.80 | 2.10 |
| 10-19 13:50 | +10 | SOL | DOWN | 0.55 | 0.80 | 2.20 |
| 10-19 13:50 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.23 |
| 10-19 13:50 | +10 stop | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-19 13:50 | +10 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-19 13:50 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-19 13:50 | +10 stop | DOGE | DOWN | 0.59 | 0.77 | 1.50 |
| 10-19 13:50 | +10 stop | XRP | DOWN | 0.57 | 0.40 | -2.05 |
| 10-19 13:49 | +10 stop | ZEC | DOWN | 0.70 | 0.55 | -1.83 |
| 10-19 13:49 | +10 stop | SOL | UP | 0.56 | 0.34 | -2.54 |
| 10-19 13:48 | +10 stop | DOGE | UP | 0.64 | 0.42 | -2.55 |
| 10-19 13:48 | +10 stop | ETH | UP | 0.56 | 0.32 | -2.74 |
| 10-19 13:48 | +10 stop | BNB | UP | 0.68 | 0.51 | -2.04 |
| 10-19 13:48 | +10 stop | XRP | UP | 0.66 | 0.49 | -2.04 |
| 10-19 13:48 | +20 | XRP | UP | 0.66 | no | -6.76 |
| 10-19 13:48 | +15 | XRP | UP | 0.66 | no | -6.76 |
| 10-19 13:48 | +10 | XRP | UP | 0.66 | no | -6.76 |
| 10-19 13:48 | +5 | XRP | UP | 0.66 | no | -6.76 |
| 10-19 13:48 | +10 stop | BTC | UP | 0.69 | 0.54 | -1.83 |
| 10-19 13:48 | +20 | BTC | UP | 0.69 | no | -7.05 |
| 10-19 13:48 | +15 | BTC | UP | 0.69 | no | -7.05 |
| 10-19 13:48 | +10 | BTC | UP | 0.69 | no | -7.05 |
| 10-19 13:48 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 10-19 13:47 | +10 stop | SOL | DOWN | 0.58 | 0.40 | -2.15 |
| 10-19 13:47 | +20 | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-19 13:47 | +15 | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-19 13:47 | +10 | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 10-19 13:47 | +5 | SOL | DOWN | 0.57 | 0.65 | 0.43 |
| 10-19 13:47 | +10 | ETH | DOWN | 0.55 | 0.66 | 0.76 |
| 10-19 13:47 | +5 | ETH | DOWN | 0.58 | 0.66 | 0.46 |
| 10-19 13:47 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.05 |
