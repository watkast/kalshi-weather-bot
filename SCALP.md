# Range-Scalp Bot

*Updated Sat Oct 24 07:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31706 | 27646 | 4060 (40) | 0 | $-9048.39 | -4.5% |
| **+10¢** | 23708 | 19016 | 4692 (58) | 0 | $-8039.82 | -5.4% |
| **+15¢** | 19847 | 14802 | 5045 (81) | 0 | $-7176.26 | -5.8% |
| **+20¢** | 17583 | 12301 | 5282 (103) | 0 | $-6368.37 | -5.8% |
| **+10¢ (15¢ stop)** | 38930 | 38871 | 59 (32) | 0 | $-14899.15 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 07:53 | +10 stop | BTC | UP | 0.56 | 0.28 | -3.13 |
| 10-24 07:52 | +10 stop | DOGE | DOWN | 0.61 | 0.85 | 2.14 |
| 10-24 07:52 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-24 07:52 | +20 | HYPE | DOWN | 0.67 | 0.92 | 2.27 |
| 10-24 07:52 | +15 | HYPE | DOWN | 0.67 | 0.92 | 2.27 |
| 10-24 07:52 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-24 07:52 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-24 07:52 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 10-24 07:52 | +20 | SOL | DOWN | 0.68 | 0.92 | 2.17 |
| 10-24 07:52 | +15 | SOL | DOWN | 0.68 | 0.92 | 2.17 |
| 10-24 07:52 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 10-24 07:52 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-24 07:52 | +10 stop | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 10-24 07:52 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 07:52 | +10 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 07:52 | +5 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-24 07:51 | +10 stop | DOGE | DOWN | 0.71 | 0.56 | -1.83 |
| 10-24 07:51 | +10 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-24 07:51 | +5 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 10-24 07:50 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 10-24 07:48 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-24 07:47 | +5 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-24 07:47 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-24 07:46 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-24 07:46 | +20 | BNB | DOWN | 0.70 | 0.94 | 2.24 |
| 10-24 07:46 | +15 | BNB | DOWN | 0.70 | 0.94 | 2.24 |
| 10-24 07:46 | +10 | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 10-24 07:46 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-24 07:46 | +10 stop | BTC | DOWN | 0.61 | 0.45 | -1.95 |
| 10-24 07:46 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-24 07:46 | +15 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 10-24 07:46 | +10 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-24 07:46 | +5 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-24 07:46 | +10 stop | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-24 07:46 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 10-24 07:46 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.43 |
| 10-24 07:46 | +10 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 10-24 07:46 | +5 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 10-24 07:46 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.77 |
| 10-24 07:46 | +20 | HYPE | DOWN | 0.65 | 0.87 | 1.92 |
