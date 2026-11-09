# Range-Scalp Bot

*Updated Mon Nov 09 14:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53812 | 46940 | 6872 (86) | 5 | $-14707.50 | -4.3% |
| **+10¢** | 40188 | 32169 | 8019 (112) | 6 | $-13703.29 | -5.4% |
| **+15¢** | 33678 | 25037 | 8641 (143) | 7 | $-12474.98 | -5.9% |
| **+20¢** | 29976 | 20911 | 9065 (189) | 7 | $-10943.18 | -5.8% |
| **+10¢ (15¢ stop)** | 65555 | 65449 | 106 (63) | 0 | $-24270.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 14:47 | +10 stop | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 11-09 14:47 | +10 stop | BTC | UP | 0.71 | 0.88 | 1.47 |
| 11-09 14:47 | +10 stop | BNB | UP | 0.65 | 0.79 | 1.12 |
| 11-09 14:47 | +10 | BNB | UP | 0.65 | 0.79 | 1.12 |
| 11-09 14:47 | +5 | BNB | UP | 0.65 | 0.71 | 0.29 |
| 11-09 14:47 | +10 stop | SOL | DOWN | 0.57 | 0.37 | -2.35 |
| 11-09 14:47 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-09 14:47 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-09 14:47 | +10 | SOL | DOWN | 0.57 | open |  |
| 11-09 14:47 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-09 14:47 | +5 | ETH | DOWN | 0.51 | open |  |
| 11-09 14:46 | +10 stop | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-09 14:46 | +20 | BNB | DOWN | 0.52 | open |  |
| 11-09 14:46 | +15 | BNB | DOWN | 0.52 | open |  |
| 11-09 14:46 | +10 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-09 14:46 | +5 | BNB | DOWN | 0.52 | 0.63 | 0.75 |
| 11-09 14:46 | +10 stop | ETH | DOWN | 0.63 | 0.38 | -2.84 |
| 11-09 14:46 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-09 14:46 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-09 14:46 | +10 | ETH | DOWN | 0.63 | open |  |
| 11-09 14:46 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 11-09 14:46 | +10 stop | XRP | DOWN | 0.61 | 0.34 | -3.03 |
| 11-09 14:46 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-09 14:46 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-09 14:46 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-09 14:46 | +5 | XRP | DOWN | 0.60 | open |  |
| 11-09 14:46 | +10 stop | ZEC | DOWN | 0.50 | 0.21 | -3.20 |
| 11-09 14:46 | +20 | ZEC | DOWN | 0.51 | open |  |
| 11-09 14:46 | +15 | ZEC | DOWN | 0.51 | open |  |
| 11-09 14:46 | +10 | ZEC | DOWN | 0.51 | open |  |
| 11-09 14:46 | +5 | ZEC | DOWN | 0.51 | 0.57 | 0.24 |
| 11-09 14:46 | +10 stop | BTC | DOWN | 0.62 | 0.35 | -3.03 |
| 11-09 14:46 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-09 14:46 | +15 | BTC | DOWN | 0.62 | open |  |
| 11-09 14:46 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-09 14:46 | +5 | BTC | DOWN | 0.62 | open |  |
| 11-09 14:46 | +10 stop | DOGE | DOWN | 0.68 | 0.42 | -2.94 |
| 11-09 14:46 | +20 | DOGE | DOWN | 0.68 | open |  |
| 11-09 14:46 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-09 14:46 | +10 | DOGE | DOWN | 0.69 | open |  |
