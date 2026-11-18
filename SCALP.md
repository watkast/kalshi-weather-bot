# Range-Scalp Bot

*Updated Wed Nov 18 09:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63939 | 55766 | 8173 (119) | 1 | $-17477.31 | -4.3% |
| **+10¢** | 47765 | 38199 | 9566 (160) | 2 | $-16384.47 | -5.5% |
| **+15¢** | 40048 | 29735 | 10313 (205) | 3 | $-14847.94 | -5.9% |
| **+20¢** | 35665 | 24840 | 10825 (260) | 4 | $-13142.61 | -5.9% |
| **+10¢ (15¢ stop)** | 77776 | 77618 | 158 (93) | 1 | $-28553.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 09:31 | +10 stop | BNB | DOWN | 0.53 | 0.70 | 1.37 |
| 11-18 09:31 | +20 | BNB | DOWN | 0.53 | open |  |
| 11-18 09:31 | +15 | BNB | DOWN | 0.53 | 0.70 | 1.37 |
| 11-18 09:31 | +10 | BNB | DOWN | 0.53 | 0.70 | 1.37 |
| 11-18 09:31 | +5 | BNB | DOWN | 0.53 | 0.70 | 1.37 |
| 11-18 09:31 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-18 09:31 | +20 | XRP | DOWN | 0.59 | open |  |
| 11-18 09:31 | +15 | XRP | DOWN | 0.59 | open |  |
| 11-18 09:31 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-18 09:31 | +5 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-18 09:30 | +10 stop | ZEC | UP | 0.63 | open |  |
| 11-18 09:30 | +20 | ZEC | UP | 0.64 | open |  |
| 11-18 09:30 | +15 | ZEC | UP | 0.64 | open |  |
| 11-18 09:30 | +10 | ZEC | UP | 0.64 | open |  |
| 11-18 09:30 | +5 | ZEC | UP | 0.64 | 0.70 | 0.28 |
| 11-18 09:30 | +10 stop | ETH | UP | 0.58 | 0.40 | -2.15 |
| 11-18 09:30 | +20 | ETH | UP | 0.58 | open |  |
| 11-18 09:30 | +15 | ETH | UP | 0.58 | open |  |
| 11-18 09:30 | +10 | ETH | UP | 0.58 | open |  |
| 11-18 09:30 | +5 | ETH | UP | 0.58 | open |  |
| 11-18 09:27 | +10 stop | BNB | UP | 0.62 | 0.94 | 2.95 |
| 11-18 09:27 | +10 | BNB | UP | 0.62 | 0.94 | 2.95 |
| 11-18 09:27 | +10 stop | XRP | UP | 0.68 | 0.53 | -1.85 |
| 11-18 09:27 | +15 | XRP | UP | 0.68 | 0.86 | 1.55 |
| 11-18 09:27 | +10 | XRP | UP | 0.69 | 0.86 | 1.46 |
| 11-18 09:27 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 11-18 09:27 | +10 stop | ZEC | DOWN | 0.40 | 0.61 | 1.76 |
| 11-18 09:27 | +10 | ZEC | DOWN | 0.40 | 0.61 | 1.76 |
| 11-18 09:27 | +5 | ZEC | DOWN | 0.40 | 0.61 | 1.76 |
| 11-18 09:27 | +10 stop | DOGE | DOWN | 0.58 | 0.31 | -3.03 |
| 11-18 09:27 | +10 | DOGE | DOWN | 0.58 | yes | -5.98 |
| 11-18 09:27 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-18 09:27 | +10 stop | XRP | DOWN | 0.50 | 0.67 | 1.36 |
| 11-18 09:27 | +15 | XRP | DOWN | 0.50 | 0.67 | 1.36 |
| 11-18 09:27 | +10 | XRP | DOWN | 0.50 | 0.67 | 1.36 |
| 11-18 09:27 | +5 | XRP | DOWN | 0.52 | 0.67 | 1.16 |
| 11-18 09:27 | +10 stop | BNB | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 09:27 | +15 | BNB | DOWN | 0.52 | yes | -5.38 |
| 11-18 09:27 | +10 | BNB | DOWN | 0.52 | 0.62 | 0.65 |
| 11-18 09:26 | +10 stop | ETH | UP | 0.54 | 0.80 | 2.30 |
