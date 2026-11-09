# Range-Scalp Bot

*Updated Mon Nov 09 11:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53623 | 46767 | 6856 (86) | 0 | $-14706.32 | -4.4% |
| **+10¢** | 40061 | 32063 | 7998 (112) | 0 | $-13685.57 | -5.4% |
| **+15¢** | 33569 | 24950 | 8619 (143) | 0 | $-12480.02 | -5.9% |
| **+20¢** | 29872 | 20830 | 9042 (189) | 1 | $-10974.67 | -5.9% |
| **+10¢ (15¢ stop)** | 65345 | 65239 | 106 (63) | 0 | $-24185.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 11:52 | +15 | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 11-09 11:52 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 0.98 |
| 11-09 11:52 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-09 11:52 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.29 |
| 11-09 11:52 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-09 11:52 | +5 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-09 11:52 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 11-09 11:52 | +10 | SOL | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 11:52 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-09 11:51 | +10 stop | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 11-09 11:51 | +10 | BNB | DOWN | 0.64 | 0.81 | 1.42 |
| 11-09 11:51 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 11:49 | +10 stop | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-09 11:49 | +20 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-09 11:49 | +15 | ZEC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-09 11:49 | +10 | ZEC | DOWN | 0.62 | 0.75 | 0.99 |
| 11-09 11:49 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.48 |
| 11-09 11:49 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-09 11:48 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 11:48 | +20 | HYPE | DOWN | 0.69 | 0.93 | 2.23 |
| 11-09 11:48 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 11:48 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 11:48 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 11-09 11:47 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-09 11:47 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 11:47 | +20 | BTC | DOWN | 0.71 | 0.95 | 2.24 |
| 11-09 11:47 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-09 11:47 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 11:47 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-09 11:47 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 11:47 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 11-09 11:46 | +10 stop | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 11-09 11:46 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 11-09 11:46 | +15 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 11-09 11:46 | +10 | NEAR | DOWN | 0.57 | 0.68 | 0.76 |
| 11-09 11:46 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 11-09 11:46 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-09 11:46 | +20 | DOGE | DOWN | 0.61 | 0.91 | 2.71 |
| 11-09 11:46 | +15 | DOGE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-09 11:46 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
