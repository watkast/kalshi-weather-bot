# Range-Scalp Bot

*Updated Wed Nov 04 04:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46798 | 40753 | 6045 (72) | 4 | $-13449.01 | -4.6% |
| **+10¢** | 34958 | 27950 | 7008 (96) | 4 | $-12272.42 | -5.6% |
| **+15¢** | 29273 | 21732 | 7541 (124) | 5 | $-11226.20 | -6.1% |
| **+20¢** | 26003 | 18105 | 7898 (164) | 7 | $-9884.75 | -6.1% |
| **+10¢ (15¢ stop)** | 57053 | 56960 | 93 (56) | 4 | $-21323.19 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 04:17 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +10 stop | BNB | DOWN | 0.61 | open |  |
| 11-04 04:16 | +20 | BNB | DOWN | 0.61 | open |  |
| 11-04 04:16 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-04 04:16 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-04 04:16 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-04 04:16 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 11-04 04:16 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-04 04:16 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-04 04:16 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-04 04:16 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-04 04:16 | +10 stop | BTC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-04 04:16 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 11-04 04:16 | +20 | ZEC | DOWN | 0.58 | open |  |
| 11-04 04:16 | +15 | ZEC | DOWN | 0.58 | open |  |
| 11-04 04:16 | +10 | ZEC | DOWN | 0.58 | open |  |
| 11-04 04:16 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-04 04:16 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-04 04:16 | +15 | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 04:16 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 04:16 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-04 04:16 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-04 04:16 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 11-04 04:16 | +5 | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 11-04 04:16 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-04 04:16 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-04 04:16 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-04 04:16 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-04 04:16 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 11-04 04:03 | +10 stop | XRP | UP | 0.59 | 0.85 | 2.34 |
| 11-04 04:03 | +10 stop | ETH | UP | 0.64 | 0.78 | 1.10 |
| 11-04 04:03 | +10 stop | BNB | UP | 0.62 | 0.78 | 1.25 |
| 11-04 04:03 | +10 stop | BTC | UP | 0.58 | 0.73 | 1.18 |
